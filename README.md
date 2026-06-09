# RAG-Powered Project Intelligence Assistant

## Overview

The RAG-Powered Project Intelligence Assistant enables users to search and query historical project repositories using natural language.

Organizations often maintain hundreds of project PowerPoint presentations containing valuable information about project domains, technology stacks, solution approaches, team sizes, durations, and business outcomes. Manually searching through these repositories is time-consuming and inefficient.

This solution converts project repositories into a searchable knowledge base using Retrieval-Augmented Generation (RAG), Semantic Search, Metadata Filtering, and Re-ranking.


## Problem Statement

Organizations store large amounts of project knowledge in PowerPoint presentations and documents.

Challenges:
- Knowledge is scattered across multiple project decks.
- Traditional keyword search cannot understand semantic meaning.
- Finding similar projects takes significant manual effort.
- Reusing previous solutions and technology choices is difficult.
- Proposal preparation and project discovery are slow.

The objective is to build an AI-powered assistant that can understand natural language questions and instantly retrieve relevant project information.


## Key Features

- Semantic Search using Vector Embeddings
- Metadata-Based Filtering
- Cross-Encoder Re-ranking
- Retrieval-Augmented Generation (RAG)
- Natural Language Question Answering
- Source-Grounded Responses
- Fast Retrieval using ChromaDB


## Architecture

### Phase 1: Knowledge Base Creation (Offline)

```text
Project PPT Repository
        │
        ▼
    PPT Parser
        │
        ▼
 Project Extractor
        │
        ▼
Metadata Extraction
        │
        ▼
Retrieval Text Builder
        │
        ▼
 BGE Embeddings
        │
        ▼
    ChromaDB
```

### Phase 2: Question Answering (Real-Time)

```text
User Query
    │
    ▼
Query Router
    │
 ┌──┴───────┐
 │          │
 ▼          ▼
Metadata  Semantic
 Filter    Search
 │          │
 └────┬─────┘
      ▼
  Re-Ranker
      ▼
Prompt Builder
      ▼
    LLM
      ▼
 Final Answer
```

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| API Framework | FastAPI |
| LLM | Llama 3.1 8B Instant (Groq) |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | ChromaDB |
| Re-Ranker | Cross-Encoder (MS MARCO MiniLM) |
| PPT Parsing | python-pptx |
| Environment | Python Virtual Environment |

---

## Project Structure

```text
project-intelligence-assistant/

├── app/
│   ├── api/
│   ├── embeddings/
│   ├── ingestion/
│   ├── llm/
│   ├── metadata/
│   ├── prompts/
│   ├── rag/
│   ├── retrieval/
│   ├── router/
│   ├── utils/
│   └── vectorstore/
│
├── data/
├── chroma_db/
├── main.py
├── requirements.txt
└── README.md
```

---

## Workflow

1. Parse PowerPoint project repositories.
2. Extract project information and metadata.
3. Generate vector embeddings.
4. Store embeddings and metadata in ChromaDB.
5. Accept user queries in natural language.
6. Route queries to metadata filtering or semantic search.
7. Retrieve relevant projects.
8. Re-rank results using a Cross Encoder.
9. Generate answers using an LLM.
10. Return structured project insights to the user.

---

## Run Backend

```bash
uvicorn app.api.app:app --reload
```

## Run Backend

```bash
streamlit run streamlit_app.py
```

## Example Queries

```text
Show healthcare AI projects

List telecom projects

Projects using AWS

How was fraud detection implemented?

Find projects similar to customer churn prediction

Show projects with Graph Neural Networks
```

---

## Bonus Features Implemented

- Semantic Search
- Metadata Filtering
- Cross-Encoder Re-ranking
- Retrieval-Augmented Generation (RAG)
- Source-Grounded Responses

---

## Future Enhancements

- Chunk-Based Retrieval
- Hybrid Search (BM25 + Vector Search)
- Confidence Scoring
- Evaluation Dashboard
- Multimodal Slide Understanding
- Interactive Chat UI

---

## Business Impact

- Reduces manual search effort.
- Improves knowledge reuse.
- Accelerates proposal preparation.
- Enables faster project discovery.
- Enhances organizational knowledge management.

---

## Authors

**Project:** RAG-Powered Project Intelligence Assistant  
**Hackathon:** ITT Hackathon 2026
