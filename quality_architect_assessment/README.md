# Quality Architect Assessment Deliverables

Generated from the uploaded assessment and repository inspection.

- `ui-manual-tests.md` — UI cases for Parts, tabs, categories, flags, units, revisions, negative/boundary flows.
- `api-manual-tests.md` — API CRUD, filtering, validation, relations, permissions, conflicts.
- `ui-automation/` — Playwright smoke/core tests.
- `api-automation/` — pytest + requests tests.
- `agent-artifacts/prompts.md` — reproducible agent workflow.

## API
```bash
cd api-automation
pip install -r requirements.txt
INVENTREE_URL=http://localhost:8000 INVENTREE_TOKEN=<token> pytest -q
```
## UI
```bash
cd ui-automation
npm install
npx playwright install
INVENTREE_URL=http://localhost:8000 npx playwright test
```
Adjust authentication/storage state and endpoint paths to the deployed instance.
