# Experiment 002: Retrieval Error Analysis

## Purpose

Analyze cases where retrieval misses the expected supporting document or returns weak context.

## Clean Workflow

Use the internship-specific retrieval-only runner:

```bash
python3 internship_work/scripts/retrieval_error_analysis.py
```

This avoids the generator and only tests retrieval. It writes:

- `results.json`: detailed per-question retrieval results.
- `summary.md`: readable summary with ranks and case labels.

To test a different retrieval depth:

```bash
python3 internship_work/scripts/retrieval_error_analysis.py --topk 1
python3 internship_work/scripts/retrieval_error_analysis.py --topk 3
```

Main config:

```text
internship_work/configs/exp_002_retrieval_error_analysis.yaml
```

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
