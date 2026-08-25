# Public release checklist

## Completed locally

- [x] Public code is isolated from the production project and runtime profile.
- [x] Examples are synthetic and contain no supplier, customer, contract or quotation data.
- [x] Runtime logs, sessions, databases, memories and credentials are excluded.
- [x] Automated privacy scan passes.
- [x] Tests and Python compilation pass.
- [x] Agent Skill frontmatter and required behavior were reviewed.
- [x] The 24-field audit schema is internally consistent.
- [x] The staged Git file list contains source, documentation and synthetic examples only.
- [x] Complete Chinese and English README files are provided and cross-linked.
- [x] The public workflow covers all ten procurement stages and four human Gates.
- [x] External RFQ sanitization and market-reference-only rules have executable tests.
- [x] `distribution.yaml`, `SOUL.md`, and bundled Skills form a native Hermes Profile Distribution.
- [x] Deployment commands were checked against the installed Hermes CLI and official distribution documentation.

## Required immediately before publishing

- [ ] Confirm the GitHub owner and final repository name.
- [ ] Review the staged diff manually one more time.
- [ ] Run `python scripts/privacy_scan.py` again.
- [ ] Confirm the Apache-2.0 license and public project attribution.
- [ ] Create the remote repository without importing unrelated files.
- [ ] Enable secret scanning, push protection and dependency alerts.
- [ ] Push only after explicit final approval.
