# Retrieval Error Analysis Summary

Run the analysis script first:

```bash
python3 internship_work/scripts/retrieval_error_analysis.py
```

After the run, this file is overwritten with the actual retrieval summary.

Expected outputs:

- `results.json`: detailed per-question retrieval output.
- `summary.md`: generated readable summary.

What to look for:

- `expected_doc_rank_1`: retrieval worked for that question.
- `expected_doc_ranked_low`: increase top-k or improve ranking.
- `expected_doc_missing`: check query wording, corpus content, index, or embedding model.
- `answer_string_found_in_other_doc`: answer-string metric may be misleading.
