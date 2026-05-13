from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass

from civicflow_ai.data import KnowledgeDocument


TOKEN_PATTERN = re.compile(r"[a-z0-9]+")
STOP_WORDS = {
    "a",
    "an",
    "and",
    "by",
    "for",
    "has",
    "have",
    "i",
    "is",
    "it",
    "my",
    "of",
    "on",
    "or",
    "the",
    "there",
    "this",
    "to",
    "was",
    "with",
}


@dataclass(frozen=True)
class SearchResult:
    document: KnowledgeDocument
    score: float


def tokenize(text: str) -> list[str]:
    return [
        token
        for token in TOKEN_PATTERN.findall(text.lower())
        if token not in STOP_WORDS and len(token) > 1
    ]


class KnowledgeRetriever:
    """Small local TF-IDF retriever used as an inspectable RAG stand-in."""

    def __init__(self, documents: list[KnowledgeDocument]) -> None:
        self.documents = documents
        self.document_vectors = [
            self._term_counts(
                f"{document.title} {document.category} {document.body} {document.summary}"
            )
            for document in documents
        ]
        self.idf = self._inverse_document_frequency()

    def search(self, query: str, limit: int = 3) -> list[SearchResult]:
        query_vector = self._term_counts(query)
        scored = [
            SearchResult(document=document, score=self._cosine_similarity(query_vector, vector))
            for document, vector in zip(self.documents, self.document_vectors)
        ]
        return sorted(scored, key=lambda item: item.score, reverse=True)[:limit]

    def _term_counts(self, text: str) -> Counter[str]:
        return Counter(tokenize(text))

    def _inverse_document_frequency(self) -> dict[str, float]:
        doc_count = len(self.documents)
        terms = set()
        for vector in self.document_vectors:
            terms.update(vector)

        idf = {}
        for term in terms:
            matching_docs = sum(1 for vector in self.document_vectors if term in vector)
            idf[term] = math.log((1 + doc_count) / (1 + matching_docs)) + 1
        return idf

    def _weighted(self, vector: Counter[str]) -> dict[str, float]:
        return {term: count * self.idf.get(term, 1.0) for term, count in vector.items()}

    def _cosine_similarity(self, left: Counter[str], right: Counter[str]) -> float:
        weighted_left = self._weighted(left)
        weighted_right = self._weighted(right)
        shared_terms = set(weighted_left) & set(weighted_right)

        numerator = sum(weighted_left[term] * weighted_right[term] for term in shared_terms)
        left_norm = math.sqrt(sum(value * value for value in weighted_left.values()))
        right_norm = math.sqrt(sum(value * value for value in weighted_right.values()))

        if left_norm == 0 or right_norm == 0:
            return 0.0

        return numerator / (left_norm * right_norm)
