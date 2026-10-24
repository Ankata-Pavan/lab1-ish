# Lab 1 — A Minimal Tool-Using Agent

Build a small tool-using agent from scratch in Python: receive a natural-language
question, decide which tool to use, call that tool, and return an answer grounded
in the tool's output. No frameworks — just the core agent loop.


---

## Repository layout

```text
.
├── agent.py            # Main agent loop (you implement)
├── tools.py            # Three tools + registry (you implement)
├── run_examples.py     # Runs test questions and writes logs/
├── design_note.md      # Written design note (you complete)
├── requirements.txt
├── .env.example
├── data/
│   ├── course_info.txt
│   └── numbers.txt
├── logs/               # Success and failure run traces (you generate)
└── README.md           # Update this with how to run *your* code
```

---

## Prerequisites

- Python 3.10+
- An OpenAI API key (or a compatible endpoint / local model via Ollama)
- Git

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # then edit .env and add your key
```

Or export the key without a `.env` file:

```bash
export OPENAI_API_KEY="sk-..."
```

Optional: `export OPENAI_MODEL="gpt-4o-mini"` (default).

## What you must implement

1. **`tools.py`** — `calculator`, `file_reader`, `lookup`, plus `TOOLS` registry and
   `build_tool_descriptions`.
2. **`agent.py`** — the Thought → Action → Observation loop that talks to the LLM,
   parses JSON tool calls / final answers, and returns a result dict.
3. **`run_examples.py`** — run at least six questions (successes and deliberate
   failures) and write readable logs under `logs/`.
4. **`README.md`** — keep this file accurate for graders (install + run commands).

Starter stubs in this repo raise `NotImplementedError` until you fill them in.
Sample `data/` files are provided for `file_reader`.

### Suggested smoke test after implementing

```bash
python agent.py "What is 2 + 2?"
python run_examples.py
```

---
 Your API key stays in
`.env` (gitignored) — never commit secrets.
