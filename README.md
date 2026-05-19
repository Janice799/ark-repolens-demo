# ARK RepoLens

Public demo for ARK RepoLens, a source-local code intelligence workflow for
private repositories. The demo indexes a tiny project, answers coding questions
with file citations, and shows how source code can stay on the user's machine.

This repository is intentionally small. It is not the full paid ARK RepoLens
delivery package and it does not include private customer code, private model
weights, commercial handoff documents, or the licensed ZIP.

## What This Shows

- A small local demo project
- The kind of `index`, `report`, `ask`, and `doctor` workflow used by ARK
  RepoLens
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

## Public Space

https://huggingface.co/spaces/JaniceMJ/ark-repolens

GitHub demo repository:

https://github.com/Janice799/ark-repolens-demo

## Demo Project

```text
examples/demo_project/
  README.md
  policy.md
  service.py
```

## Why This Is Different From A Base Model

Open code models can answer general coding questions. ARK RepoLens adds a
local product workflow around approved model paths: repository indexing,
citation-backed answers, secret redaction reporting, buyer delivery manifests,
commercial handoff documents, and a customization path for customer-specific
model or adapter work.

## Full Product Access

The paid ARK RepoLens package starts with an ARK RepoLens PayPal payment link. After
payment is confirmed, THE ARK delivers private repository access or a licensed
ZIP with install docs, delivery checklist, commercial handoff documents,
configuration files, and upgrade path.

Request access:

https://www.ark-deck.com/code

Visual workflow:

https://www.ark-deck.com/code#workflow-demo

## License

This public demo is provided for evaluation. The full ARK RepoLens commercial
package is delivered under separate paid terms.
