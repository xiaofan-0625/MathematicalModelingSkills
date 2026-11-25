---
name: submission-packaging
description: Assemble and audit a mathematical-modeling competition submission package for rule compliance, anonymity, filenames, clean rebuilds, manifests, hashes, and archive integrity. Use only for final delivery or a submission dry run.
---

# Package the Final Submission

Treat the current official rules as the only authority for filenames, formats, page limits, anonymity, supplementary files, and AI-use declarations. Packaging does not authorize an external upload.

## Workflow

1. Freeze the accepted source revision and record the official submission rules with their source and access date.
2. Build the final PDF and allowed attachments from a clean copy. Re-run the reproducibility and cross-file consistency checks.
3. Copy only allowed deliverables into `提交/`. Exclude caches, temporary files, private data, credentials, local absolute paths, hidden author metadata, and unrequested source assets.
4. Check filenames, extensions, file count, size, page count, fonts, links, embedded metadata, anonymity, and required declarations.
5. Generate a manifest containing relative path, role, byte size, SHA-256, producing source, and validation status.
6. Create the archive only if required. Extract it into a fresh temporary directory, compare its manifest, open the PDF, and sample-run the documented reproduction command.
7. Record the final checklist and unresolved exceptions. Do not claim submission or upload unless that external action was actually completed and authorized.

## Gate

G7 passes only when all official requirements are mapped to evidence, the clean-build result matches the reviewed PDF, the package contains no prohibited material, hashes are stable, and the extracted archive passes inspection.

Read [submission-packaging.md](../../references/submission-packaging.md) for the manifest schema, anonymity audit, and release checklist.
