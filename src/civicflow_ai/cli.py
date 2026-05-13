from __future__ import annotations

import argparse

from civicflow_ai.assistant import CivicAssistant


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="civicflow-ai",
        description="Triage a local-government service request.",
    )
    parser.add_argument("request", help="Citizen request text to triage")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    response = CivicAssistant().handle_request(args.request)

    print(f"Category: {response.triage.category}")
    print(f"Priority: {response.triage.priority}")
    print(f"Confidence: {response.triage.confidence:.2f}")
    print(f"Escalate: {'yes' if response.triage.escalate else 'no'}")
    print()
    print("Evidence:")
    for item in response.context:
        print(f"- {item.document.title} ({item.score:.2f})")
    print()
    print("Draft response:")
    print(response.draft_response)
