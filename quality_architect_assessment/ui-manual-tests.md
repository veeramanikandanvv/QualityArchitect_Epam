# UI Manual Test Cases — Parts

| ID | Scenario | Steps | Expected | Pri |
|---|---|---|---|---|
| UI-001 | Create part | New Part; enter name/IPN/category; save | Created and listed | P0 |
| UI-002 | Required validation | Submit blank form | Inline errors; no create | P0 |
| UI-003 | Duplicate IPN | Create existing IPN | Clear rejection | P0 |
| UI-004 | Import | Upload CSV; map; preview; commit | Valid rows created; invalid rows reported | P0 |
| UI-005 | Import boundaries | Blank, duplicate, over-length values | Row-level errors; no silent loss | P1 |
| UI-006 | Overview | Open part detail | Identity, flags, stock summary/actions visible | P0 |
| UI-007 | Stock tab | Add/edit/remove stock | Quantities/location/history correct | P0 |
| UI-008 | BOM tab | Add child; edit quantity; remove | Correct BOM; self/circular refs rejected | P0 |
| UI-009 | Allocated | Open tab with allocations | Accurate allocation rows | P1 |
| UI-010 | Build Orders | Open tab with build order | Related orders visible | P1 |
| UI-011 | Parameters | Add/edit/remove parameter and unit | Values persist and validate | P0 |
| UI-012 | Variants | Create variant from template | Link and constraints correct | P1 |
| UI-013 | Revisions | Create revision/code | Unique codes and restrictions enforced | P0 |
| UI-014 | Attachments | Upload/view/delete | Metadata, permissions correct | P1 |
| UI-015 | Related Parts | Add/remove relation | Relation visible as expected | P1 |
| UI-016 | Test Templates | Attach template; inspect results | Association/results visible | P1 |
| UI-017 | Categories | Parent/child; filter | Hierarchy/counts correct | P0 |
| UI-018 | Parametric table | Filter by parameter/unit; combine | Matching set only; clear restores | P1 |
| UI-019 | Flags | Toggle Virtual, Template, Assembly, Component, Trackable, Purchaseable, Salable, Active | Persistence and dependent rules correct | P0 |
| UI-020 | Inactive part | Attempt stock/BOM/order actions | Restricted operations blocked | P0 |
| UI-021 | Units | Compatible/incompatible units | Conversion works; invalid rejected | P1 |
| UI-022 | Revision circularity | Revision-of-revision/circular link | Rejected without partial write | P0 |
| UI-023 | Read-only user | Create/edit/delete/import | UI and API deny mutation | P0 |
| UI-024 | Cross-functional | Create part → parameter → stock → category | Connected data visible end-to-end | P0 |
| UI-025 | Search/paging | Search, sort, paginate many parts | Stable, complete results | P1 |
| UI-026 | Resilience/a11y | Keyboard navigation; delayed save; double click | Focus/labels; no duplicate submit; recoverable errors | P1 |

Evidence: screenshot/video, request/response, IDs, console errors, build/version, feature flags.
