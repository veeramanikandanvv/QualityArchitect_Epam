from langchain_core.tools import tool

from ..context.models import MemoryRecord
from ..context.persistence import MemoryStore


@tool
def retrieve_project_memory(query: str, memory_root: str = "memory") -> str:
    """Retrieve relevant project memory. Results retain confidence and source metadata."""
    store = MemoryStore(memory_root)
    records = store.search(query)
    if not records:
        return "No matching project memory found."
    return "\n".join(
        f"[{r['confidence']}] {r['content']} | source={r['source']}"
        for r in records
    )


@tool
def save_project_memory(
    category: str,
    content: str,
    source: str,
    confidence: str = "unverified",
    memory_root: str = "memory",
) -> str:
    """Persist a decision, finding, assumption, or evidence note."""
    MemoryStore(memory_root).save_record(
        MemoryRecord(category=category, content=content, source=source, confidence=confidence)
    )
    return "Memory record saved."
