# Day 1 FlashRAG Progress

## Setup
- Forked/cloned FlashRAG in WSL.
- Created Python virtual environment.
- Installed project in editable mode.
- Added `.venv/` to `.gitignore`.

## Corpus processing
- Ran `chunk_doc_corpus.py`.
- Processed 14,406 documents into 135,040 chunks.

## Index building
- Installed `faiss-cpu`.
- Built an E5 retrieval index using `intfloat/e5-base-v2`.
- Index saved under `indexes/e5_test`.

## Next steps
- Inspect retriever configuration.
- Connect `indexes/e5_test` in `my_config.yaml`.
- Run a small retrieval test.
- Then run a minimal RAG pipeline.