from __future__ import annotations

from dataclasses import dataclass

from civicflow_ai.data import KNOWLEDGE_BASE
from civicflow_ai.retrieval import KnowledgeRetriever, SearchResult
from civicflow_ai.triage import TriageResult, triage_request


@dataclass(frozen=True)
class AssistantResponse:
    request: str
    triage: TriageResult
    context: list[SearchResult]
    draft_response: str


class CivicAssistant:
    """Coordinates retrieval, triage, and response drafting."""

    def __init__(self) -> None:
        self.retriever = KnowledgeRetriever(KNOWLEDGE_BASE)

    def handle_request(self, request: str) -> AssistantResponse:
        if not request.strip():
            raise ValueError("request must not be empty")

        context = self.retriever.search(request, limit=2)
        triage = triage_request(request, context)
        draft_response = self._draft_response(request, triage, context)

        return AssistantResponse(
            request=request,
            triage=triage,
            context=context,
            draft_response=draft_response,
        )

    def _draft_response(
        self,
        request: str,
        triage: TriageResult,
        context: list[SearchResult],
    ) -> str:
        best_context = context[0].document if context else None
        opening = "Thanks for reporting this."

        if triage.escalate:
            action = (
                "I have flagged it for human review because it may involve urgency, "
                "safety risk, or low classification confidence."
            )
        else:
            action = "I have grouped it for the service team to review and action."

        if best_context:
            guidance = f"The most relevant guidance I found is: {best_context.summary}"
        else:
            guidance = "I could not find a strong matching policy snippet."

        return (
            f"{opening} {action} {guidance} "
            f"Reference category: {triage.category}. Original request: {request}"
        )
