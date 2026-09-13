from .models import AssessmentContext
from .persistence import MemoryStore


def build_subagent_context(
    task: str,
    context: AssessmentContext,
    memory: MemoryStore,
) -> str:
    records = memory.search(task)
    memory_text = "\n".join(
        f"- [{item['confidence']}] {item['content']} (source: {item['source']})"
        for item in records
    ) or "No matching historical memory was found."

    return f"""Task: {task}
Target system: {context.target_system}
Assessment ID: {context.assessment_id}
Input documents: {', '.join(context.input_documents) or 'none recorded'}
Completed tasks: {', '.join(context.completed_tasks) or 'none'}
Existing artifacts: {', '.join(context.generated_artifacts) or 'none'}
Known assumptions: {', '.join(context.assumptions) or 'none'}

Relevant project memory:
{memory_text}

Rules:
- Treat unverified memory as a hypothesis, not a fact.
- Do not claim execution without captured evidence.
- Record new decisions, findings, and assumptions explicitly.
- Prefer existing artifacts over duplicating work.
"""
