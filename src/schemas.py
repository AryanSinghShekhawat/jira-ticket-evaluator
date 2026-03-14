from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class Verdict(str, Enum):
    PASS = "Pass"
    PARTIAL = "Partial" 
    FAIL = "Fail"

class RequirementEval(BaseModel):
    requirement: str
    verdict: Verdict
    evidence: List[str]
    confidence: float = Field(ge=0.0, le=1.0)

class EvaluationResult(BaseModel):
    overall_verdict: Verdict
    per_requirement: List[RequirementEval]
    tests: List[str] | None = None
