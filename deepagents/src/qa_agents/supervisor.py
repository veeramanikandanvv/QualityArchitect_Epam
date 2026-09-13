from pathlib import Path
from typing import Any

from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI

from .tools.memory_tools import retrieve_project_memory, save_project_memory
from .tools.qa_tools import (
    append_finding,
    inspect_artifact,
    mark_execution_evidence,
    read_source_file,
    write_qa_artifact,
)


COMMON_TOOLS = [read_source_file, write_qa_artifact, retrieve_project_memory, save_project_memory]

SPECIALISTS = [
    {
        "name": "requirements_analyst",
        "description": "Extract acceptance criteria, risks, and traceability from the assessment brief and documentation.",
        "system_prompt": "Analyze the supplied assessment and documentation. Produce a requirements matrix with risks, assumptions, and coverage priorities. Read source files before making claims.",
        "tools": COMMON_TOOLS,
    },
    {
        "name": "ui_test_designer",
        "description": "Design manual UI tests for InvenTree Parts.",
        "system_prompt": "Create reviewable manual UI tests covering part creation/import, all detail tabs, categories, flags, units, revisions, negative cases, and boundaries. Include preconditions and expected results.",
        "tools": COMMON_TOOLS,
    },
    {
        "name": "api_test_designer",
        "description": "Design manual API tests from the InvenTree schema.",
        "system_prompt": "Create positive, negative, and boundary API cases with request data, status assertions, response assertions, and cleanup requirements. Do not invent unavailable endpoints.",
        "tools": COMMON_TOOLS,
    },
    {
        "name": "api_automation",
        "description": "Draft or review executable API automation.",
        "system_prompt": "Create maintainable pytest API automation with fixtures, parameterization, explicit assertions, and environment-based configuration. Inspect existing artifacts and do not invent unavailable endpoints.",
        "tools": COMMON_TOOLS + [inspect_artifact],
    },
    {
        "name": "ui_automation",
        "description": "Draft or review Playwright UI automation.",
        "system_prompt": "Create robust Playwright tests using accessible or stable selectors, explicit waits, assertions, cleanup, and at least one cross-functional Parts flow. Inspect existing artifacts before duplicating work.",
        "tools": COMMON_TOOLS + [inspect_artifact],
    },
    {
        "name": "review_evidence",
        "description": "Review artifacts for traceability, completeness, and runnable instructions.",
        "system_prompt": "Review all outputs against the assessment phases. Identify gaps, unsupported assumptions, flaky patterns, missing assertions, and missing execution evidence. Produce a concise remediation list.",
        "tools": COMMON_TOOLS + [inspect_artifact, append_finding, mark_execution_evidence],
    },
]


def build_supervisor(model_name: str = "gpt-4o-mini"):
    model = ChatOpenAI(model=model_name, temperature=0)
    return create_deep_agent(
        model=model,
        subagents=SPECIALISTS,
        system_prompt=(
            "You are the supervising QA Architect for the InvenTree Parts assessment. "
            "Use the specialist subagents deliberately, preserve traceability to the brief, "
            "and write final artifacts under the requested output directory. "
            "Never claim tests ran unless execution evidence is available. "
            "Start by delegating requirements analysis, then design, automation, and review. "
            "Each specialist has task-specific tools; require them to use tools for source reading, "
            "artifact writing, memory retrieval, and evidence recording rather than fabricating outputs."
        ),
    )


def run_assessment(input_path: str, output_dir: str, model_name: str = "gpt-4o-mini") -> Any:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    agent = build_supervisor(model_name)
    prompt = f"""Assess the InvenTree Parts module using the source at {input_path}.

Produce a complete QA work product in {output_dir}, including:
1. requirements and risk matrix;
2. manual UI tests;
3. manual API tests;
4. API automation proposal or implementation;
5. Playwright UI automation proposal or implementation;
6. traceability and review findings.

Read the source before making assumptions. If a live target is unavailable, clearly label artifacts as drafts and list the required environment variables. Use the bound tools to read inputs, write artifacts, retrieve/save project memory, and record evidence."""
    return agent.invoke({"messages": [{"role": "user", "content": prompt}]})
