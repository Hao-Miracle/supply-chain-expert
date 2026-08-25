# Security and data publication boundary

## Public material

- Generic source code and public documentation.
- Synthetic examples unrelated to any real company, person, supplier, customer, contract, quotation or project.
- Data schemas without production records.
- Tests constructed solely for software behavior.

## Material that must remain private

- Runtime profiles, environment variables, authentication files and service configuration.
- Session databases, response stores, logs, prompts, memories and tool outputs.
- Real procurement lists, quotations, costs, contracts, supplier or customer records.
- Human-reviewed enterprise classification knowledge and correction history.
- Data intellectual-property registration evidence and trusted timestamp payloads.

## Release checklist

1. Build the release from this isolated directory, never from a runtime profile.
2. Scan filenames and contents for credentials, personal information and business identifiers.
3. Confirm every example is synthetic and has no source-row relationship to production data.
4. Review the complete Git index before committing.
5. Run tests and dependency/license checks.
6. Enable GitHub secret scanning and push protection before accepting contributions.

If sensitive material is detected, stop the release. Remove it before the first public commit and rotate any exposed credential.
