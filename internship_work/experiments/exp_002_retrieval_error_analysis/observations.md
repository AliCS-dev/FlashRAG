# Observations

## Dataset Cleanup

The original golden answers were not good for retrieval metric evaluation because they contained typos or wording that did not appear in the corpus.

Examples:

```text
retreival -> retrieval
effiecent -> efficient
similiar -> similarity
```

I updated the dataset so each golden answer is a clean substring from the expected document. This makes answer-string-based retrieval metrics easier to interpret.

## Case Notes

Question: What is Machine Learning?
Expected doc id: 0
Expected rank: 1
Retrieved docs: Machine Learning, FAISS, Retrieval Augmented Generation
Case type: expected_doc_rank_1
Observation: The retriever found the correct document first. After cleaning the golden answer, the answer string should also be found in the Machine Learning document.
Next action: Treat this case as a successful retrieval example.

Question: What is RAG?
Expected doc id: 1
Expected rank: 1
Retrieved docs: Retrieval Augmented Generation, FAISS, Machine Learning
Case type: expected_doc_rank_1
Observation: The retriever found the correct RAG document first. The previous metric failure was caused by typo/wording mismatch in the golden answer.
Next action: Treat this case as a successful retrieval example.

Question: What is FAISS used for?
Expected doc id: 2
Expected rank: 1
Retrieved docs: FAISS, Retrieval Augmented Generation, Machine Learning
Case type: expected_doc_rank_1
Observation: The retriever found the correct FAISS document first. The question wording and golden answer are now cleaner.
Next action: Treat this case as a successful retrieval example.

## Main Takeaway

Retrieval is working on this tiny custom dataset. The earlier bad retrieval metric came from poor golden answers, not from the retriever.
