from app.models import ValidationIssue


def compare_payloads(
    legacy_payload: dict, transformed_payload: dict
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    legacy_fields = set(legacy_payload.keys())
    transformed_fields = set(transformed_payload.keys())

    missing_in_transformed = sorted(legacy_fields - transformed_fields)
    missing_in_legacy = sorted(transformed_fields - legacy_fields)

    for field in missing_in_transformed:
        issues.append(
            ValidationIssue(
                field=field,
                legacy_value=legacy_payload.get(field),
                transformed_value=None,
                issue_type="missing_field",
            )
        )

    for field in missing_in_legacy:
        issues.append(
            ValidationIssue(
                field=field,
                legacy_value=None,
                transformed_value=transformed_payload.get(field),
                issue_type="missing_field",
            )
        )

    for field in sorted(legacy_fields & transformed_fields):
        legacy_value = legacy_payload.get(field)
        transformed_value = transformed_payload.get(field)
        if legacy_value != transformed_value:
            issues.append(
                ValidationIssue(
                    field=field,
                    legacy_value=legacy_value,
                    transformed_value=transformed_value,
                    issue_type="value_mismatch",
                )
            )

    return issues
