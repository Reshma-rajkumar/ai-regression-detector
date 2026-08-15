from fastapi import FastAPI

from app.sample_data import LEGACY_INVOICE, TRANSFORMED_INVOICE
from app.scoring import calculate_confidence_score
from app.validator import compare_payloads

app = FastAPI(title="enterprise-transformation-validator")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/legacy/invoice")
def get_legacy_invoice() -> dict:
    return LEGACY_INVOICE


@app.get("/transformed/invoice")
def get_transformed_invoice() -> dict:
    return TRANSFORMED_INVOICE


@app.get("/validate/invoice")
def validate_invoice() -> dict:
    legacy_invoice = get_legacy_invoice()
    transformed_invoice = get_transformed_invoice()
    issues = compare_payloads(legacy_invoice, transformed_invoice)
    issue_count = len(issues)
    confidence_score = calculate_confidence_score(issues)
    summary = (
        f"Detected {issue_count} schema mismatches between legacy and transformed payloads."
    )
    return {
        "status": "success" if not issues else "partial_match",
        "confidence_score": confidence_score,
        "issues": issues,
        "issue_count": issue_count,
        "summary": summary,
    }
