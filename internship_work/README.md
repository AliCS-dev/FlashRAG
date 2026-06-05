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
| `templates/` | Reusable file templates used by `scripts/start_day.py`. |

## Daily Workflow

Start each day from the repo root:

```bash
python3 internship_work/scripts/start_day.py --focus "what I want to work on today"
```

If you are starting a new experiment:

```bash
python3 internship_work/scripts/start_day.py \
  --focus "retrieval debugging" \
  --experiment "retrieval error analysis"
```

This creates:

- `notes/daily/YYYY-MM-DD.md` for the day.
- `experiments/exp_NNN_name/` with `README.md`, `commands.md`, `observations.md`, `summary.md`, and `config.yaml`.
- `configs/exp_NNN_name.yaml` as a shared config copy.

## Rules Of Thumb

1. Start every day with a daily note.
2. Put each experiment in exactly one `experiments/exp_NNN_name/` folder.
3. Put exact commands in `commands.md` before or after running them.
4. Put qualitative findings in `observations.md`.
5. Put the final result and next steps in `summary.md`.
6. Keep large generated outputs in repo-level `output/`, `results/`, or `indexes/`.
7. Move code into `flashrag/` only after an internship script becomes stable and reusable.

## Current Experiments

### `exp_001_custom_retrieval`

Purpose: test FlashRAG retrieval using a small custom dataset and inspect whether the correct supporting documents are retrieved.

Status: initial custom dataset and retrieval comparison completed.

### `exp_002_retrieval_error_analysis`

Purpose: analyze failed or weak retrieval cases and identify whether problems come from data, corpus content, embedding/index settings, or retrieval depth.

Status: scaffolded for future work.
