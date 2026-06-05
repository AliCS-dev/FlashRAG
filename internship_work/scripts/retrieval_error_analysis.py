import argparse
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from flashrag.config import Config
from flashrag.evaluator.utils import normalize_answer
from flashrag.utils import get_dataset, get_retriever


DEFAULT_CONFIG = REPO_ROOT / "internship_work/configs/exp_002_retrieval_error_analysis.yaml"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "internship_work/experiments/exp_002_retrieval_error_analysis"


def resolve_repo_path(path_value):
    path = Path(path_value)
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def validate_config_paths(config):
    required_paths = {
        "dataset_path": Path(config["dataset_path"]) / "test.jsonl",
        "corpus_path": config["corpus_path"],
        "index_path": config["index_path"],
    }
    missing = []
    for name, path_value in required_paths.items():
        path = resolve_repo_path(path_value)
        if not path.exists():
            missing.append(f"{name}: {path}")
    if missing:
        joined = "\n".join(missing)
        raise FileNotFoundError(f"Missing required path(s):\n{joined}")


def doc_id(doc):
    value = doc.get("id")
    return str(value) if value is not None else None


def answer_hit(doc, golden_answers):
    contents = normalize_answer(doc.get("contents", ""))
    return any(normalize_answer(answer) in contents for answer in golden_answers)


def expected_rank(retrieved_docs, expected_doc_id):
    if expected_doc_id is None:
        return None
    expected = str(expected_doc_id)
    for rank, doc in enumerate(retrieved_docs, start=1):
        if doc_id(doc) == expected:
            return rank
    return None


def classify_case(rank, answer_found, expected_doc_id):
    if rank == 1:
        return "expected_doc_rank_1"
    if rank is not None:
        return "expected_doc_ranked_low"
    if answer_found:
        return "answer_string_found_in_other_doc"
    if expected_doc_id is None:
        return "no_expected_doc_id_to_check"
    return "expected_doc_missing"


def analyze_item(item, docs):
    expected_doc_id = item.metadata.get("expected_doc_id")
    rank = expected_rank(docs, expected_doc_id)
    answer_found = any(answer_hit(doc, item.golden_answers) for doc in docs)
    return {
        "id": item.id,
        "question": item.question,
        "golden_answers": item.golden_answers,
        "expected_doc_id": expected_doc_id,
        "expected_rank": rank,
        "answer_string_found": answer_found,
        "case_type": classify_case(rank, answer_found, expected_doc_id),
        "retrieved_docs": [
            {
                "rank": idx,
                "id": doc.get("id"),
                "title": doc.get("title"),
                "answer_string_found": answer_hit(doc, item.golden_answers),
                "contents": doc.get("contents", ""),
            }
            for idx, doc in enumerate(docs, start=1)
        ],
    }


def write_markdown(results, output_path, topk):
    total = len(results)
    expected_hits = sum(1 for item in results if item["expected_rank"] is not None)
    top1_hits = sum(1 for item in results if item["expected_rank"] == 1)
    answer_hits = sum(1 for item in results if item["answer_string_found"])

    lines = [
        "# Retrieval Error Analysis Summary",
        "",
        f"- Dataset size: {total}",
        f"- Retrieval top-k: {topk}",
        f"- Expected document found in top-k: {expected_hits}/{total}",
        f"- Expected document at rank 1: {top1_hits}/{total}",
        f"- Golden answer string found in top-k: {answer_hits}/{total}",
        "",
        "## Cases",
        "",
    ]

    for item in results:
        lines.extend(
            [
                f"### {item['id']}: {item['question']}",
                "",
                f"- Expected doc id: {item['expected_doc_id']}",
                f"- Expected rank: {item['expected_rank']}",
                f"- Case type: {item['case_type']}",
                f"- Golden answers: {item['golden_answers']}",
                "",
                "| Rank | Doc id | Title | Answer string found |",
                "| --- | --- | --- | --- |",
            ]
        )
        for doc in item["retrieved_docs"]:
            lines.append(
                f"| {doc['rank']} | {doc['id']} | {doc['title']} | {doc['answer_string_found']} |"
            )
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    os.chdir(REPO_ROOT)

    parser = argparse.ArgumentParser(description="Run retrieval-only error analysis for internship experiment 002.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Path to the experiment YAML config.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Directory for analysis artifacts.")
    parser.add_argument("--topk", type=int, default=None, help="Override retrieval_topk from the config.")
    args = parser.parse_args()

    config_overrides = {"disable_save": True, "save_intermediate_data": False}
    if args.topk is not None:
        config_overrides["retrieval_topk"] = args.topk
        config_overrides["metric_setting"] = {"retrieval_recall_topk": args.topk}

    config = Config(config_file_path=args.config, config_dict=config_overrides)
    validate_config_paths(config)

    dataset = get_dataset(config)["test"]
    if dataset is None:
        raise RuntimeError(f"No test split loaded from {config['dataset_path']}")

    retriever = get_retriever(config)
    retrieval_results = retriever.batch_search(dataset.question, num=config["retrieval_topk"])
    results = [analyze_item(item, docs) for item, docs in zip(dataset, retrieval_results)]

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    results_path = output_dir / "results.json"
    summary_path = output_dir / "summary.md"

    results_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(results, summary_path, config["retrieval_topk"])

    print(f"Wrote {results_path}")
    print(f"Wrote {summary_path}")


if __name__ == "__main__":
    main()
