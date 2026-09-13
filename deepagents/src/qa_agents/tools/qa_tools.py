from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from langchain_core.tools import tool


_ALLOWED_ARTIFACT_ROOT = Path(".").resolve()


def _safe_path(path: str) -> Path:
    candidate = Path(path).resolve()
    if _ALLOWED_ARTIFACT_ROOT not in candidate.parents and candidate != _ALLOWED_ARTIFACT_ROOT:
        raise ValueError("Path must remain inside the current workspace")
    return candidate


@tool
def read_source_file(path: str) -> str:
    """Read a UTF-8 source file before deriving requirements or test cases."""
    file_path = _safe_path(path)
    if not file_path.is_file():
        return f"Source file not found: {path}"
    return file_path.read_text(encoding="utf-8")


@tool
def write_qa_artifact(path: str, content: str) -> str:
    """Write a QA artifact such as a test plan, matrix, or automation draft."""
    file_path = _safe_path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return f"QA artifact written: {file_path}"


@tool
def append_finding(path: str, finding: str, severity: str = "medium") -> str:
    """Append a structured finding to a JSONL review log."""
    file_path = _safe_path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    record: dict[str, Any] = {"finding": finding, "severity": severity}
    with file_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return f"Finding recorded: {file_path}"


@tool
def inspect_artifact(path: str) -> str:
    """Inspect an existing artifact and return its text for review or traceability."""
    return read_source_file.invoke(path)


@tool
def mark_execution_evidence(path: str, evidence: str, status: str = "unverified") -> str:
    """Record execution evidence without claiming a run occurred unless evidence exists."""
    return append_finding.invoke(
        {
            "path": path,
            "finding": f"execution_status={status}; evidence={evidence}",
            "severity": "info",
        }
    )
