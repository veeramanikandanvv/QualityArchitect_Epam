# API Requirements and Acceptance Criteria

The API assessment covers Parts CRUD, validation, permissions, and consistency. API manual scenarios and automation live under `../test-design/` and `../automation/api/`.

## P0 acceptance criteria

- List and retrieve operations return the expected schema and status codes.
- Valid creation persists a part and returns an identifiable record.
- Invalid, blank, duplicate, and unauthorized mutations are rejected without partial writes.
- Response payloads are parsed once and assertions verify stable, documented fields.
- Test evidence includes request, response, status, record ID, and environment/build details.

Live execution requires a reachable InvenTree instance and configured credentials; repository changes alone do not prove runtime behavior.
