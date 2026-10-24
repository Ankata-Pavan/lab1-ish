"""Minimal tool-using agent loop.

The agent receives a natural-language question, asks an LLM to either call a
tool or produce a final answer (as JSON), executes the requested tool, feeds
the observation back, and repeats until it gets a final answer or hits the
step limit. No frameworks — a loop with an API call inside.
"""

from __future__ import annotations

import json
import os
import sys

from tools import TOOLS, build_tool_descriptions

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # pragma: no cover
    pass

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover
    OpenAI = None


MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = """\
You are a helpful assistant with access to tools.

{tool_descriptions}

Rules:
- When you need to use a tool, respond ONLY with a JSON object in this exact format:
  {{"tool": "<tool_name>", "args": {{"<arg_name>": "<arg_value>"}}}}
- When you have a final answer and do not need any more tools, respond ONLY with:
  {{"final_answer": "<your answer>"}}
- Do not mix prose and JSON. Choose one or the other.
- Use at most 5 tool calls per question.
"""


def run_agent(question: str, max_steps: int = 5, verbose: bool = True) -> dict:
    """Run the agent on a single question.

    Returns a dict with keys:
      - success (bool)
      - answer (str | None)
      - trace (list of step records)

    Implement the Thought → Action → Observation loop:
      1. Build messages with the system prompt and user question.
      2. Call the chat completions API (temperature=0 recommended).
      3. Parse the model reply as JSON.
      4. If ``final_answer`` → return success.
      5. If ``tool`` → look up TOOLS, call it, append observation, continue.
      6. Stop after ``max_steps`` or on unparseable replies.
    """
    raise NotImplementedError("Implement run_agent(question, ...)")


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print('Usage: python agent.py "Your question here"')
        return 2

    question = " ".join(argv)
    result = run_agent(question, verbose=True)
    print(json.dumps(result, indent=2))
    return 0 if result.get("success") else 1


if __name__ == "__main__":
    raise SystemExit(main())
