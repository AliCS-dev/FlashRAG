# Commands

## Dataset cleanup

Cleaned the custom test dataset so each `golden_answers` value is a correct substring of the expected corpus document.

Edited:

```text
internship_work/datasets/my_tests/test.jsonl
```

## Retrieval-only analysis

Run the default retrieval-only analysis:

```bash
python3 internship_work/scripts/retrieval_error_analysis.py
```

Compare top-k settings:

```bash
python3 internship_work/scripts/retrieval_error_analysis.py --topk 1
python3 internship_work/scripts/retrieval_error_analysis.py --topk 3
```

## Expected output files

```text
internship_work/experiments/exp_002_retrieval_error_analysis/results.json
internship_work/experiments/exp_002_retrieval_error_analysis/summary.md
```
