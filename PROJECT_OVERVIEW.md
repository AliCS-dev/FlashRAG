# FlashRAG Project Overview

This file is a practical map of this checkout. It is meant to help you quickly find the right place to read, edit, or store internship work without changing the upstream FlashRAG package layout.

## Start Here

- `flashrag/` is the main Python package. Most library behavior lives here.
- `examples/` contains runnable examples from the original project.
- `docs/` contains project documentation and extra notes.
- `webui/` contains the Gradio-based UI.
- `internship_work/` is your personal workspace for experiments, notes, custom datasets, and scripts.
- `datasets/`, `indexes/`, `models/`, `output/`, and `results/` are local runtime/data folders. They can become large and are intentionally ignored by git.

## Main Code Areas

| Path | Purpose |
| --- | --- |
| `flashrag/config/` | Configuration loading and default settings. |
| `flashrag/dataset/` | Dataset loading and dataset object helpers. |
| `flashrag/retriever/` | Dense/sparse retrieval, index building, encoders, rerankers. |
| `flashrag/generator/` | LLM generation backends and generation utilities. |
| `flashrag/pipeline/` | RAG pipeline orchestration, including sequential, active, branching, reasoning, and multimodal pipelines. |
| `flashrag/prompt/` | Prompt templates and example prompts. |
| `flashrag/evaluator/` | Metrics and evaluation logic. |
| `flashrag/refiner/` | Context compression/refinement components. |
| `flashrag/judger/` | Judging/routing helpers used by some advanced pipelines. |
| `flashrag/utils/` | Shared utility functions and constants. |

## Personal Work Area

Use `internship_work/` for anything that is not part of the reusable FlashRAG library:

| Path | Use For |
| --- | --- |
| `internship_work/configs/` | Experiment-specific YAML configs. |
| `internship_work/datasets/` | Small custom datasets for experiments. JSONL files are currently ignored by git. |
| `internship_work/scripts/` | One-off runners, debugging scripts, preprocessing helpers. |
| `internship_work/experiments/` | One folder per experiment, with notes, configs, and result summaries. |
| `internship_work/notes/` | Daily notes and understanding checkpoints. |

Recommended experiment structure:

```text
internship_work/experiments/exp_###_short_name/
  README.md
  observations.md
  config.yaml
  commands.md
```

Keep large generated files in `output/`, `results/`, `indexes/`, `models/`, or ignored dataset folders. Keep small explanations and reproducibility notes in `internship_work/experiments/...`. If a dataset is important but ignored, describe it in the experiment README or add a tiny non-sensitive sample separately.

## Common Commands

Install the project in editable mode:

```bash
pip install -e .
```

Run the quick English demo:

```bash
python examples/quick_start/demo_en.py
```

Build a dense retrieval index:

```bash
python -m flashrag.retriever.index_builder \
  --retrieval_method e5 \
  --model_path intfloat/e5-base-v2 \
  --corpus_path indexes/my_test_corpu.jsonl \
  --save_dir indexes/e5_my_test
```

Run a custom experiment script from the repo root:

```bash
python my_test_pipline.py --model_path models/llama3-8b-instruct --retriever_path intfloat/e5-base-v2
```

## Files To Treat Carefully

- `flashrag/config/basic_config.yaml`: global defaults used by the package.
- `flashrag/pipeline/pipeline.py`: central pipeline behavior.
- `flashrag/retriever/retriever.py`: retrieval logic used by many pipelines.
- `flashrag/evaluator/metrics.py`: metric definitions and evaluation behavior.
- `setup.py`, `pyproject.toml`, `requirements.txt`: packaging and dependency setup.

## Current Local Notes

There are local/generated artifacts in this checkout:

- `my_test_pipline.py` and `mytestconfig.yaml` are custom root-level experiment files.
- `domainrag_text_corpus.jsonl`, `datasets/`, `indexes/`, `models/`, `output/`, and `results/` are local data/output areas and are ignored by git.
- `internship_work/` is currently untracked and appears to be the intended organized workspace for your internship material.

When in doubt, add notes under `internship_work/` first, then promote reusable code into `flashrag/` only after the experiment is stable.
