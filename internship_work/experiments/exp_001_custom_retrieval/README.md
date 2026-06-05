# Experiment 001: Custom Retrieval

## Purpose

Test FlashRAG retrieval with a small custom dataset and check whether the expected supporting documents are retrieved.

## Inputs

- Dataset: `internship_work/datasets/my_tests/test.jsonl`
- Related corpus/index artifacts currently live under repo-level ignored folders such as `indexes/`.

## What This Experiment Checks

- Whether the retriever can find the expected document for each question.
- Whether `retrieval_topk` is high enough for the custom dataset.
- Whether document wording in the corpus matches the question wording closely enough.

## Status

Initial custom dataset and retrieval comparison completed.

## Next Steps

- Save the exact command used to run the experiment in `commands.md`.
- Copy the exact config used for the successful run into this folder.
- Add examples of good and bad retrieval cases to `observations.md`.
