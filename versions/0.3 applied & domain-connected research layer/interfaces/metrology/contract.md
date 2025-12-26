# Metrology Contract

## Input
- MeasurementRecords (aus physics/)
- zu messende Größen + Einheitenanforderungen
- Geräte-/Sensorinformationen (falls vorhanden)

## Output
1) UnitRecord
- quantity_name
- dimension (z.B. L, T, M)
- unit (SI/derived)
- scale_type (ratio/intervall/...)
- allowed transformations

2) CalibrationRecord
- instrument
- reference standard
- calibration date
- drift assumptions
- traceability chain

3) TraceabilityReport
- ok | incomplete
- missing links

## Akzeptanzkriterien
- jede Messgröße hat Einheit + Dimension
- jede systematische Unsicherheit hat Quelle (Kalibrierung/Drift/etc.)

