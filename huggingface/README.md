---
title: ARK RepoLens Demo
emoji: 🧭
colorFrom: blue
colorTo: gray
sdk: static
pinned: false
license: other
short_description: Local repo indexing with cited code answers.
---

# ARK RepoLens Demo

ARK RepoLens is a public demo of ARK LocalEngine, a source-local repo
intelligence workflow for private repositories. It indexes a tiny demo project,
answers coding questions with file citations, and keeps source code on the
user's machine.

This is not a new base model release. It is a demo of a productized local code
workflow that can run on top of approved open or local model paths. Base model
weights keep their own upstream licenses.

## Public Demo

GitHub demo repository:

https://github.com/Janice799/ark-localengine-demo

## What The Demo Shows

- Local repository indexing
- Citation-backed coding answers
- Secret redaction reporting in the index summary
- A buyer-readable transcript for the local workflow
- The difference between a generic code model and a source-local product
  workflow

## Demo Question

```text
Where is checkout_total implemented?
```

The demo answer cites:

- `examples/demo_project/service.py:1-17`
- `examples/demo_project/README.md:1-12`

## Commands

```bash
localengine index examples/demo_project
localengine report
localengine doctor
localengine ask "Where is checkout_total implemented?"
```

## Full Commercial Kit

The paid ARK RepoLens package includes private repo or licensed ZIP delivery, install
docs, delivery checklist, commercial handoff templates, configuration files, and
an upgrade path for customer-specific model or adapter work.

Request access on THE ARK:

https://www.ark-deck.com/code

## Boundary

This public demo does not include private customer code, private model weights,
paid delivery ZIPs, or commercial handoff templates.
