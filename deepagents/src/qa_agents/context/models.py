from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class AssessmentContext:
    assessment_id: str
    target_system: str = "InvenTree Parts"
    input_documents: list[str] = field(default_factory=list)
    completed_tasks: list[str] = field(default_factory=list)
    generated_artifacts: list[str] = field(default_factory=list)
    findings: list[dict[str, Any]] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


@dataclass
class MemoryRecord:
    category: str
    content: str
    source: str
    confidence: str = "unverified"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict[str, str]:
        return self.__dict__.copy()
