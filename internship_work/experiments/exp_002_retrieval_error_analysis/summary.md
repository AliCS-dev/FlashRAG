# Retrieval Error Analysis Summary

- Dataset size: 3
- Retrieval top-k: 3
- Expected document found in top-k: 3/3
- Expected document at rank 1: 3/3
- Golden answer string found in top-k: 3/3

## Cases

### test0: What is Machine Learning?

- Expected doc id: 0
- Expected rank: 1
- Case type: expected_doc_rank_1
- Golden answers: ['Machine Learning refers to computer systems that learn patterns from data']

| Rank | Doc id | Title | Answer string found |
| --- | --- | --- | --- |
| 1 | 0 | Machine Learning | True |
| 2 | 2 | FAISS | False |
| 3 | 1 | Retrieval Augmented Generation | False |

### test1: What is RAG?

- Expected doc id: 1
- Expected rank: 1
- Case type: expected_doc_rank_1
- Golden answers: ['Retrieval Augmented Generation, also called RAG']

| Rank | Doc id | Title | Answer string found |
| --- | --- | --- | --- |
| 1 | 1 | Retrieval Augmented Generation | True |
| 2 | 2 | FAISS | False |
| 3 | 0 | Machine Learning | False |

### test2: What is FAISS used for?

- Expected doc id: 2
- Expected rank: 1
- Case type: expected_doc_rank_1
- Golden answers: ['FAISS is used for efficient similarity search']

| Rank | Doc id | Title | Answer string found |
| --- | --- | --- | --- |
| 1 | 2 | FAISS | True |
| 2 | 1 | Retrieval Augmented Generation | False |
| 3 | 0 | Machine Learning | False |
