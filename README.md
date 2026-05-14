# ARK RepoLens

Public demo for ARK RepoLens, an ARK LocalEngine product for private
repositories. The demo indexes a tiny project, answers coding questions with
file citations, and shows how source code can stay on the user's machine.

This repository is intentionally small. It is not the full paid ARK LocalEngine
delivery package and it does not include private customer code, private model
weights, commercial handoff templates, or the licensed ZIP.

## What This Shows

- A small local demo project
- The kind of `index`, `report`, `ask`, and `doctor` workflow used by ARK
  LocalEngine
- Citation-backed answers instead of generic model guesses
- The difference between a base code model and a productized local coding
  workflow

## Demo Question

```text
Where is checkout_total implemented?
```

The demo answer points to:

- `examples/demo_project/service.py:1-17`
- `examples/demo_project/README.md:1-12`

See `transcripts/demo_transcript.md` for the full example output.

## Demo Project

```text
examples/demo_project/
  README.md
  policy.md
  service.py
```

## Why This Is Different From A Base Model

Open code models can answer general coding questions. ARK LocalEngine adds a
local product workflow around approved model paths: repository indexing,
citation-backed answers, secret redaction reporting, buyer delivery manifests,
commercial handoff documents, and a customization path for customer-specific
model or adapter work.

## Full Commercial Kit

The paid ARK RepoLens package includes the private repository or licensed ZIP
delivery, install docs, delivery checklist, commercial handoff templates,
configuration files, and upgrade path.

Request access:

https://www.ark-deck.com/code

## License

This public demo is provided for evaluation. The full ARK LocalEngine commercial
package is delivered under separate paid terms.
