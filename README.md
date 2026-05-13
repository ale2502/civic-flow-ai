# CivicFlow AI

A personal AI portfolio project focused on practical Python, retrieval, classification, and human-reviewed automation.

## Project pitch

CivicFlow AI is a small assistant for local-government service teams. It reads a citizen request, retrieves relevant council policy context, classifies the request, flags risk or urgency, and drafts a response that a human operator can review.

The goal is not to replace staff. The goal is to reduce repetitive triage work, make service responses more consistent, and show how AI can be applied safely in a real business workflow.

## Technical focus

This project was built to practise core skills used in modern AI application development:

- Python package structure and command-line tooling
- Retrieval-augmented generation concepts
- Text classification and confidence scoring
- Human-review escalation for responsible AI workflows
- Clean separation between data, retrieval, triage, and response generation
- Tests for expected behaviour
- A roadmap toward APIs, containers, cloud deployment, and real LLM integration

The current implementation is intentionally lightweight:

- `src/civicflow_ai/retrieval.py` implements a small TF-IDF retrieval layer that behaves like a simple local vector search.
- `src/civicflow_ai/triage.py` classifies requests and adds escalation signals.
- `src/civicflow_ai/assistant.py` combines retrieval plus triage into a RAG-style workflow.
- `src/civicflow_ai/cli.py` provides a quick demo path.
- The roadmap below shows next steps for FastAPI, Docker, LLM APIs, cloud deployment, and CI.

## Quick start

```bash
python3 -m civicflow_ai "There is a fallen tree blocking the footpath outside 12 King Street."
```

For local development:

```bash
PYTHONPATH=src python3 -m civicflow_ai "My recycling bin was missed yesterday."
python3 -m unittest
```

## Example output

```text
Category: roads_and_paths
Priority: high
Confidence: 0.84
Escalate: yes

Draft response:
Thanks for reporting this. I found guidance about urgent hazards on public paths...
```

## Portfolio story for interviews

I built CivicFlow AI as a practical proof of concept for service operations. It takes unstructured customer requests, retrieves relevant policy context, classifies the request, and drafts a reviewable response. I started with a dependency-light local implementation so the workflow is easy to inspect and test, then designed the project so the retrieval layer can later be swapped for real embeddings and a vector database.

The main lesson was that an AI feature is only useful when it fits the workflow around it. So I added confidence scores, escalation flags, and citations to source snippets instead of returning an unchecked answer.

## Suggested next build steps

1. Add a FastAPI endpoint: `POST /triage`.
2. Replace TF-IDF retrieval with embeddings using OpenAI, Azure OpenAI, or Ollama.
3. Store documents and request logs in SQLite or PostgreSQL.
4. Add Docker and a GitHub Actions test workflow.
5. Add an evaluation dataset with expected categories and escalation decisions.
6. Deploy to Azure App Service or AWS App Runner.

## Resume bullet

Built `CivicFlow AI`, a Python proof of concept that applies RAG-style retrieval, text classification, confidence scoring, and human-review escalation to local-government service requests; designed for future integration with LLM APIs, vector databases, CI/CD, containers, and cloud deployment.
