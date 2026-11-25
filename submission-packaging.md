# Submission Packaging Protocol

Use this protocol for a dry run and again for the final accepted revision. Do not infer submission rules from a prior year.

## Rule matrix

Create one row per official requirement:

| Requirement | Official source/location | Expected value | Evidence checked | Status |
|---|---|---|---|---|
| file name and extension | | | | |
| PDF/page/size limit | | | | |
| anonymity and metadata | | | | |
| allowed attachments | | | | |
| code/data requirements | | | | |
| declarations | | | | |
| submission channel and deadline | | | | |

If official requirements conflict, stop and surface the conflict instead of choosing silently.

## Clean build

Start from protected inputs and the accepted source revision in a fresh directory. Install or use only documented dependencies. Run the declared build and reproduction commands, compare results with recorded tolerances, and verify that the PDF under review is the PDF being packaged.

Do not include build caches, notebooks with hidden state as the only implementation, editor settings, credentials, private raw data, local environment files, absolute paths, or unlicensed assets unless the rules explicitly require and permit them.

## Anonymity and privacy audit

Inspect visible text and document/archive metadata for names, student or school identifiers, emails, account names, machine paths, author fields, comments, tracked changes, EXIF data, notebook outputs, and filenames. Search source and final artifacts separately. Required identifiers and declarations are exceptions only when the current rules say so.

## Manifest

Use relative paths and include:

```json
{
  "package_version": "1",
  "built_at_utc": "ISO-8601",
  "files": [
    {
      "path": "paper.pdf",
      "role": "primary_submission",
      "bytes": 12345,
      "sha256": "...",
      "produced_from": ["论文/论文.tex"],
      "checks": {"opens": true, "anonymity": "pass", "rules": "pass"}
    }
  ]
}
```

Generate hashes after the last modification. A changed file invalidates its earlier hash and any archive verification.

## Archive verification

If an archive is required:

1. create it from the staged `提交/` contents, not the working tree;
2. reject absolute paths and parent traversal entries;
3. extract into a fresh temporary directory;
4. compare file list, sizes, and SHA-256 values with the manifest;
5. open the primary PDF and inspect representative attachments;
6. execute the shortest documented smoke reproduction when required.

## Release record

Record accepted source revision, build command, environment summary, rule-matrix result, visual-QA result, manifest path, archive hash, unresolved exceptions, and responsible reviewer. “Package ready” means local checks passed; “submitted” additionally requires observed external submission evidence such as a receipt or accepted status.
