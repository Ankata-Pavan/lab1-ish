"""Tool definitions and registry for the minimal tool-using agent.

Implement three tools and a registry the agent can pass (as text) to the LLM.
Tools should return strings — including error messages — rather than raising,
so the agent loop can feed failures back as observations.
"""

from __future__ import annotations

import math
import os
from typing import Callable


def calculator(expression: str) -> str:
    """Evaluate a mathematical expression and return the result as a string.

    Hint: a restricted ``eval`` with ``math`` helpers (and empty ``__builtins__``)
    is acceptable for this lab. Catch exceptions and return ``Error: ...``.
    """
    raise NotImplementedError("Implement calculator(expression)")


def file_reader(filename: str) -> str:
    """Read a text file from the local ``data/`` directory and return its contents.

    Hint: resolve paths under ``data/`` next to this file. Reject path traversal
    (e.g. ``../``). On missing files, return an error string instead of raising.
    """
    raise NotImplementedError("Implement file_reader(filename)")


def lookup(query: str) -> str:
    """Look up a fact from a small local knowledge base.

    Include roughly 10–15 entries. Matching policy (substring vs exact key) is
    a design choice — document it in ``design_note.md``.
    """
    raise NotImplementedError("Implement lookup(query)")


# Maps tool name -> (callable, description for the LLM)
TOOLS: dict[str, tuple[Callable[..., str], str]] = {
    "calculator": (
        calculator,
        "Evaluates a mathematical expression. Input: a string like '2 + 2' or "
        "'sqrt(16)'. Returns the numeric result.",
    ),
    "file_reader": (
        file_reader,
        "Reads a text file from the data/ directory. Input: a filename string "
        "like 'notes.txt'. Returns file contents.",
    ),
    "lookup": (
        lookup,
        "Looks up a factual query in a local knowledge base. Input: a topic "
        "string like 'python' or 'UB'. Returns a short description.",
    ),
}


def build_tool_descriptions(tools: dict) -> str:
    """Convert the tool registry into a prompt-ready description string."""
    raise NotImplementedError("Implement build_tool_descriptions(tools)")
