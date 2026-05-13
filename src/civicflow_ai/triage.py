from __future__ import annotations

from dataclasses import dataclass

from civicflow_ai.retrieval import SearchResult


URGENT_TERMS = {
    "blocked",
    "danger",
    "dangerous",
    "emergency",
    "exposed",
    "fallen",
    "flood",
    "flooding",
    "hazard",
    "injured",
    "risk",
    "unsafe",
}


@dataclass(frozen=True)
class TriageResult:
    category: str
    priority: str
    confidence: float
    escalate: bool


def triage_request(request: str, context: list[SearchResult]) -> TriageResult:
    top_match = context[0] if context else None
    confidence = top_match.score if top_match else 0.0
    category = top_match.document.category if top_match and confidence > 0 else "unknown"
    urgent = any(term in request.lower() for term in URGENT_TERMS)

    if urgent:
        priority = "high"
    elif confidence < 0.15:
        priority = "needs_review"
    else:
        priority = "normal"

    return TriageResult(
        category=category,
        priority=priority,
        confidence=confidence,
        escalate=urgent or confidence < 0.15,
    )
