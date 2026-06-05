# Experiment 002: Retrieval Error Analysis

## Purpose

Analyze cases where retrieval misses the expected supporting document or returns weak context.

## Suggested Questions

- Which questions fail because no relevant document is retrieved?
- Which questions retrieve a relevant document but rank it too low?
- Are failures caused by dataset wording, corpus content, embedding model behavior, or index settings?
- Does increasing `retrieval_topk` improve recall?

## Suggested Artifacts

- `commands.md`: exact commands run.
- `config.yaml`: config used for the run.
- `observations.md`: qualitative findings and examples.
- `summary.md`: final conclusion and next steps.
