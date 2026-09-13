# API Manual Test Cases — Parts

| ID | Scenario | Expected |
|---|---|---|
| API-001 | List parts | 200 response with paginated results |
| API-002 | Create valid part | 201 response and persisted part |
| API-003 | Missing required fields | 400 validation response |
| API-004 | Duplicate IPN | Conflict or validation rejection |
| API-005 | Retrieve part | Correct identity and fields |
| API-006 | Update part | Authorized update persists |
| API-007 | Delete part | Authorized deletion succeeds |
| API-008 | Read-only user mutation | 403/401 response |
| API-009 | Invalid identifier | 404 response |
| API-010 | Pagination/filtering | Stable and complete results |

Evidence: request, response, status, headers, IDs, server logs, build/version, feature flags.
