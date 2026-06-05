# Datasets

Store small local datasets for internship experiments here.

Important: this repository currently ignores `*.jsonl` files globally, so JSONL datasets in this folder are local-only by default. That is useful for large or temporary data, but remember to document dataset shape and purpose in experiment notes.

Suggested dataset format for FlashRAG test files:

```jsonl
{"id": "0", "question": "...", "golden_answers": ["..."]}
```
