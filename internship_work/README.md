# FlashRAG Internship Work

This folder is the workspace for internship-specific material. Keep custom experiments here so the upstream FlashRAG code remains easy to compare, update, and understand.

## Folder Structure

| Path | Purpose |
| --- | --- |
| `configs/` | Custom YAML configs for experiments. |
| `datasets/` | Small custom datasets used for testing retrieval and RAG pipelines. JSONL files are ignored by git by default. |
| `scripts/` | Helper scripts for testing, preprocessing, evaluation, and debugging. |
| `experiments/` | One folder per experiment, with notes, configs, commands, and summaries. |
| `notes/` | Daily notes and technical understanding. |

## Workflow

1. Create or choose an experiment folder under `experiments/`.
2. Put the exact config and command notes in that folder.
3. Keep large generated outputs in the repo-level `output/`, `results/`, or `indexes/` folders.
4. Record observations as you go so you can reconstruct what changed later.
5. Move reusable code into `flashrag/` only after the experiment is stable.

## Current Experiments

### `exp_001_custom_retrieval`

Purpose: test FlashRAG retrieval using a small custom dataset and inspect whether the correct supporting documents are retrieved.

Status: initial custom dataset and retrieval comparison completed.

### `exp_002_retrieval_error_analysis`

Purpose: analyze failed or weak retrieval cases and identify whether problems come from data, corpus content, embedding/index settings, or retrieval depth.

Status: scaffolded for future work.
