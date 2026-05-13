from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KnowledgeDocument:
    id: str
    title: str
    category: str
    body: str
    summary: str


KNOWLEDGE_BASE: list[KnowledgeDocument] = [
    KnowledgeDocument(
        id="roads-urgent-hazard",
        title="Urgent road and footpath hazards",
        category="roads_and_paths",
        body=(
            "Fallen trees, blocked footpaths, exposed wires, flooding, potholes, "
            "sinkholes, traffic signal faults, and hazards affecting public safety "
            "should be prioritised for urgent inspection."
        ),
        summary="urgent hazards on roads or public paths should be inspected quickly.",
    ),
    KnowledgeDocument(
        id="waste-missed-bin",
        title="Missed bin collection",
        category="waste",
        body=(
            "Missed rubbish, recycling, or green waste bins can be logged when the "
            "bin was presented on time and collection has not occurred by the end "
            "of the scheduled day."
        ),
        summary="missed rubbish or recycling collections can be logged for follow-up.",
    ),
    KnowledgeDocument(
        id="parks-maintenance",
        title="Parks and public space maintenance",
        category="parks",
        body=(
            "Damaged playground equipment, broken park furniture, overgrown public "
            "areas, graffiti, and unsafe public space issues should be routed to "
            "parks maintenance."
        ),
        summary="park damage, graffiti, and unsafe public spaces go to parks maintenance.",
    ),
    KnowledgeDocument(
        id="animals-noise",
        title="Animal and noise complaints",
        category="compliance",
        body=(
            "Recurring barking, nuisance noise, wandering animals, and potential "
            "bylaw breaches should be recorded with location, time, and supporting "
            "details before compliance review."
        ),
        summary="noise and animal complaints need details for compliance review.",
    ),
]
