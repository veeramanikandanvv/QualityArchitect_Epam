# API Manual Test Cases — Parts

| ID | Test | Expected |
|---|---|---|
| API-001 | Unauthenticated list | 401/403 |
| API-002 | Authenticated list | 200; pagination schema |
| API-003 | Search exact/partial name/IPN | Matching results only |
| API-004 | Filter category/active/template/assembly | Correct set |
| API-005 | Pagination boundaries | Safe/default or validation behavior |
| API-006 | Minimal valid create | 201/200; server fields present |
| API-007 | Missing required field | 400 field error |
| API-008 | Max/over max lengths | Boundary accepted; excess rejected |
| API-009 | Null/blank/unknown foreign key | Schema/business validation |
| API-010 | Duplicate IPN | 400/409; no duplicate |
| API-011 | Detail existing/missing | 200/404 |
| API-012 | PATCH mutable field | Only intended field changes |
| API-013 | Read-only field mutation | Rejected/ignored per schema |
| API-014 | Delete | 204/200; subsequent state documented |
| API-015 | Category CRUD | Correct hierarchy and status codes |
| API-016 | Category self/circular parent | Rejected; hierarchy unchanged |
| API-017 | Category/location/supplier relations | Valid accepted; invalid rejected |
| API-018 | Revision unique code | Created and linked |
| API-019 | Revision circular/duplicate constraints | Rejected; no partial write |
| API-020 | Part flags | Business rules enforced |
| API-021 | Read-only permissions | 401/403; no mutation |
| API-022 | Bad JSON/content type | 400/415 |
| API-023 | Repeat/conflict requests | No unintended duplicates |
| API-024 | Schema contract | Types, nullable/read-only/paging conform |
