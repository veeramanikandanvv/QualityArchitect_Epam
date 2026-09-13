# DeepAgents QA Orchestrator

A LangChain DeepAgents supervisor that delegates the InvenTree Parts assessment to specialist subagents.

## Agents

- **Supervisor / QA Architect** — plans the run, delegates tasks, and coordinates artifacts.
- **Requirements Analyst** — extracts acceptance criteria and risk areas from the assessment brief and Parts documentation.
- **UI Test Designer** — produces manual UI coverage for CRUD, tabs, flags, categories, units, revisions, negative and boundary cases.
- **API Test Designer** — produces manual API cases from the schema.
- **API Automation** — writes or reviews executable API tests.
- **UI Automation** — writes or reviews Playwright coverage.
- **Review / Evidence** — checks traceability, assertions, and runnable commands.

## Run

```bash
cd deepagents
python -m venv .venv
. .venv/bin/activate
pip install -e .
cp .env.example .env
qa-assess --input ../README.md --output ./generated
```

Set `OPENAI_API_KEY`. Optional settings include `OPENAI_MODEL`, `INVENTREE_URL`, `INVENTREE_TOKEN`, and `DRY_RUN`.

The orchestrator writes Markdown artifacts under the output directory. It does not claim live execution unless the target URL and credentials are configured.
