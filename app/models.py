from typing import Literal

from pydantic import BaseModel, Field


class TransformationInput(BaseModel):
    org_name: str
    current_state: str
    target_state: str
    initiatives: list[str] = Field(default_factory=list)


class ValidationResult(BaseModel):
    is_valid: bool
    issues: list[str] = Field(default_factory=list)
    score: float


class ValidationIssue(BaseModel):
    field: str
    legacy_value: object | None = None
    transformed_value: object | None = None
    issue_type: Literal["missing_field", "value_mismatch"]
