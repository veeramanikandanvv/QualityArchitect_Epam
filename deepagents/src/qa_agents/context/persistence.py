import json
from pathlib import Path
from typing import Any

from .models import AssessmentContext, MemoryRecord


class MemoryStore:
    """Git-reviewable memory store using JSONL and Markdown/YAML files."""

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.records_path = self.root / "records.jsonl"
        self.context_path = self.root / "latest-context.json"

    def save_record(self, record: MemoryRecord) -> None:
        with self.records_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record.to_dict(), ensure_ascii=False) + "\n")

    def search(self, query: str, limit: int = 8) -> list[dict[str, Any]]:
        if not self.records_path.exists():
            return []
        terms = {term.lower() for term in query.split() if term.strip()}
        matches: list[dict[str, Any]] = []
        for line in self.records_path.read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            haystack = f"{record.get('category', '')} {record.get('content', '')}".lower()
            if not terms or any(term in haystack for term in terms):
                matches.append(record)
        return matches[-limit:]

    def save_context(self, context: AssessmentContext) -> None:
        self.context_path.write_text(
            json.dumps(context.to_dict(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
