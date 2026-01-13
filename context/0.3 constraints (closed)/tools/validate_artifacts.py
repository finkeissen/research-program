#!/usr/bin/env python3
"""
Validate artifact envelopes (JSON) and bundles (JSONL) against the envelope schema + record schemas.

Usage:
  python validate_artifacts.py --schemas ./schemas --input ./schemas/examples/walkthrough_bundle.jsonl
  python validate_artifacts.py --schemas ./schemas --input ./some_artifact.json

Requires:
  pip install jsonschema
"""
from __future__ import annotations
import argparse
import json
import os
from typing import Any, Dict, Tuple

from jsonschema import Draft202012Validator

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def iter_jsonl(path: str):
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield lineno, json.loads(line)
            except json.JSONDecodeError as e:
                raise SystemExit(f"[FAIL] {path}:{lineno} invalid JSON: {e}")

def load_schemas(schemas_root: str) -> Tuple[Draft202012Validator, Dict[str, Draft202012Validator]]:
    env_path = os.path.join(schemas_root, "envelope", "envelope.schema.json")
    if not os.path.exists(env_path):
        raise SystemExit(f"[FAIL] envelope schema not found: {env_path}")

    env_schema = load_json(env_path)
    env_validator = Draft202012Validator(env_schema)

    record_validators: Dict[str, Draft202012Validator] = {}
    records_dir = os.path.join(schemas_root, "records")
    if not os.path.isdir(records_dir):
        raise SystemExit(f"[FAIL] records dir not found: {records_dir}")

    for fn in os.listdir(records_dir):
        if not fn.endswith(".schema.json"):
            continue
        schema = load_json(os.path.join(records_dir, fn))
        # filename convention: <type>.schema.json (supports snake_case types like decision_space)
        rec_type = fn.split(".")[0]
        record_validators[rec_type] = Draft202012Validator(schema)

    return env_validator, record_validators

def validate_one(obj: Dict[str, Any], env_v: Draft202012Validator, rec_vs: Dict[str, Draft202012Validator], where: str) -> int:
    env_errs = sorted(env_v.iter_errors(obj), key=lambda e: e.path)
    if env_errs:
        print(f"[FAIL] Envelope errors at {where}:")
        for e in env_errs:
            print(f"  - {list(e.path)}: {e.message}")
        return len(env_errs)

    rec_type = obj.get("type")
    payload = obj.get("payload")
    if not isinstance(payload, dict):
        print(f"[FAIL] {where}: payload must be an object")
        return 1

    if rec_type not in rec_vs:
        print(f"[FAIL] {where}: no record schema for type='{rec_type}'. Have: {sorted(rec_vs.keys())}")
        return 1

    rec_errs = sorted(rec_vs[rec_type].iter_errors(payload), key=lambda e: e.path)
    if rec_errs:
        print(f"[FAIL] Record errors ({rec_type}) at {where}:")
        for e in rec_errs:
            print(f"  - {list(e.path)}: {e.message}")
        return len(rec_errs)

    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schemas", required=True, help="Path to schemas/ directory (contains envelope/ and records/).")
    ap.add_argument("--input", required=True, help="Path to .json or .jsonl artifact(s).")
    args = ap.parse_args()

    env_v, rec_vs = load_schemas(args.schemas)

    total_errors = 0
    if args.input.endswith(".jsonl"):
        count = 0
        for lineno, obj in iter_jsonl(args.input):
            where = f"{args.input}:{lineno}"
            total_errors += validate_one(obj, env_v, rec_vs, where)
            count += 1
        if total_errors == 0:
            print(f"[OK] {count} artifact(s) validated successfully.")
        else:
            print(f"[FAIL] {total_errors} validation error(s) across {count} artifact(s).")
            raise SystemExit(1)
    else:
        obj = load_json(args.input)
        total_errors += validate_one(obj, env_v, rec_vs, args.input)
        if total_errors == 0:
            print("[OK] artifact validated successfully.")
        else:
            print(f"[FAIL] {total_errors} validation error(s).")
            raise SystemExit(1)

if __name__ == "__main__":
    main()
