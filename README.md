# AI Regression Detector

Enterprise programs increasingly use AI to transform critical business systems, but leadership teams need evidence they can trust. This project provides a simple validation layer to compare legacy and transformed payloads and surface schema mismatches clearly.

## Problem Statement

Enterprises need confidence that AI-driven transformations preserve business-critical data structures. Without a validation checkpoint, silent field drift can break downstream reporting, finance controls, and operational workflows.

## What This MVP Does

This FastAPI MVP validates a transformed invoice against a legacy invoice by:
- detecting missing and extra fields
- flagging value mismatches for common fields
- generating a confidence score
- returning structured, human-readable issues

## Endpoints

- `GET /health` - service status check
- `GET /legacy/invoice` - sample legacy invoice payload
- `GET /transformed/invoice` - sample transformed invoice payload
- `GET /validate/invoice` - validation result with score, issue count, and summary

## Sample Validation Response

```json
{
  "status": "partial_match",
  "confidence_score": 0,
  "issues": [
    {
      "field": "customer",
      "legacy_value": "Acme Enterprises",
      "transformed_value": null,
      "issue_type": "missing_field"
    }
  ],
  "issue_count": 9,
  "summary": "Detected 9 schema mismatches between legacy and transformed payloads."
}
```

**Field meanings**
- `status`: `success` when no issues are found, otherwise `partial_match`
- `confidence_score`: integer score derived from issue count
- `issues`: structured mismatch details for debugging and audit
- `issue_count`: total number of detected issues
- `summary`: concise sentence for dashboards and stakeholders

## Why This Matters for ERP/CRM Transformation

ERP and CRM modernization projects involve high-value entities (orders, invoices, customers, contracts). Even small schema mismatches can cascade into billing errors, compliance gaps, and broken integrations. A validator like this provides an early warning layer before transformed data reaches production systems.

## Future Improvements

- support nested and deeply typed schema validation
- add configurable field-mapping rules and tolerance policies
- produce diff reports and transformation quality trends over time
- integrate with CI/CD gates for automated release blocking
- extend coverage to additional domains (orders, customers, inventory)

## Architecture

```text
Legacy Payload --> Validator Engine <-- Transformed Payload
                          |
                          v
               Issue Detection + Confidence Score
                          |
                          v
                    Validation Summary
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```
