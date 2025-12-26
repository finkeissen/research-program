# Schema Validation Tooling

This folder contains a minimal validator script to check artifact envelopes (JSON) and bundles (JSONL)
against the project schemas.

## Install

pip install jsonschema

## Validate a bundle

python validate_artifacts.py --schemas ../../schemas --input ../../schemas/examples/walkthrough_bundle.jsonl

## Validate a single artifact

python validate_artifacts.py --schemas ../../schemas --input ../../schemas/examples/claim.json

## Notes
- Record schemas are discovered by filename: <type>.schema.json
- This supports snake_case types such as decision_space and atomic_problem

