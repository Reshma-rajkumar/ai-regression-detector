from fastapi.testclient import TestClient

from app.main import app
from app.sample_data import LEGACY_INVOICE, TRANSFORMED_INVOICE
from app.validator import compare_payloads

client = TestClient(app)


def test_compare_payloads_detects_missing_fields_for_renamed_keys():
    issues = compare_payloads(LEGACY_INVOICE, TRANSFORMED_INVOICE)
    assert issues

    issue_by_field = {issue.field: issue for issue in issues}
    for field in ("customer", "invoice_date", "items", "total_amount"):
        assert field in issue_by_field
        assert issue_by_field[field].issue_type == "missing_field"

    transformed_fields = [issue.field for issue in issues if issue.issue_type == "missing_field"]
    assert "client_name" in transformed_fields
    assert "date" in transformed_fields
    assert "line_items" in transformed_fields
    assert "amount_due" in transformed_fields


def test_validate_invoice_endpoint_returns_partial_match():
    response = client.get("/validate/invoice")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "partial_match"
    assert data["confidence_score"] < 100
    assert len(data["issues"]) >= 8
    assert data["issue_count"] == len(data["issues"])
    assert data["summary"] == (
        f"Detected {data['issue_count']} schema mismatches "
        "between legacy and transformed payloads."
    )
