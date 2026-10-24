"""Run a battery of test questions through the agent and log every result.

Usage:
    python run_examples.py

Each question's full trace is printed to the console and also written to a
file in ``logs/``. Mix questions that should succeed, a multi-step question,
and questions that should fail or be ambiguous.

You may edit the question list, but your submission must include at least
three success logs and two failure logs.
"""

from __future__ import annotations

import json
import os

from agent import run_agent

LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")

# (filename, question) pairs. Filenames match the submission requirements.
QUESTIONS = [
    # Should succeed: calculator
    ("success_1.txt", "What is 1247 divided by 43, rounded to 2 decimal places?"),
    # Should succeed: file reader
    ("success_2.txt", "What does the file 'course_info.txt' say?"),
    # Should succeed: lookup
    ("success_3.txt", "Tell me something about the University at Buffalo."),
    # Interesting: requires two steps (read file, then add the numbers)
    ("success_4.txt", "Read the file 'numbers.txt' and tell me the sum of all numbers in it."),
    # Should fail / be ambiguous: no tool really fits
    ("failure_1.txt", "What is the meaning of life?"),
    # Should fail gracefully: file does not exist
    ("failure_2.txt", "Read the file 'secrets.txt' and summarize it."),
]


def format_result(question: str, result: dict) -> str:
    """Render a question + result dict as a readable plain-text log."""
    lines = [
        "=" * 60,
        f"Question: {question}",
        "=" * 60,
        "",
        "Trace:",
    ]
    for entry in result.get("trace", []):
        etype = entry.get("type")
        step = entry.get("step")
        if etype == "tool_call":
            lines.append(
                f"  [step {step}] TOOL CALL -> {entry.get('tool')}({entry.get('args')})"
            )
        elif etype == "observation":
            lines.append(f"  [step {step}] OBSERVATION: {entry.get('content')}")
        elif etype == "final":
            lines.append(f"  [step {step}] FINAL ANSWER: {entry.get('content')}")
        elif etype == "error":
            lines.append(f"  [step {step}] ERROR (unparseable): {entry.get('content')}")
        else:
            lines.append(f"  [step {step}] {entry}")
    lines.extend(
        [
            "",
            f"success: {result.get('success')}",
            f"answer:  {result.get('answer')}",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    os.makedirs(LOG_DIR, exist_ok=True)

    for filename, question in QUESTIONS:
        print(f"\n{'=' * 60}")
        print(f"Question: {question}")
        result = run_agent(question, verbose=True)
        print(f"\nResult: {json.dumps(result, indent=2)}")

        path = os.path.join(LOG_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(format_result(question, result))
        print(f"(logged to {os.path.relpath(path)})")


if __name__ == "__main__":
    main()
