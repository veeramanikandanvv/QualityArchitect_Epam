# UI Requirements and Acceptance Criteria

The UI assessment covers Parts workflows and cross-functional behavior. The canonical scenarios are in [`../test-design/ui-manual-tests.md`](../test-design/ui-manual-tests.md).

## P0 acceptance criteria

- Users can create a part with valid required fields.
- Required-field, duplicate-IPN, inactive-part, permission, unit, revision-circularity, and dependent-rule validations are enforced.
- Overview, stock, BOM, parameters, categories, revisions, and connected workflows preserve data accurately.
- Search, paging, and cross-functional flows return complete and stable results.
- Failed saves and repeated submissions do not create duplicate or partial records.

## Evidence

Capture screenshots or video, request/response pairs, record IDs, console errors, build/version, and feature flags for each executed scenario.
