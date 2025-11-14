# Auto Blog Writer

A small experiment showing how multiple agents work together to reduce LLM hallucination and produce higher-quality outputs by splitting responsibilities (outline → draft → edit).

## Project structure
- `main.py` — pipeline implementation and entrypoint (`async def main()`).
- `requirements.txt` — Python dependencies.
- `.env` — environment variables (store API_KEY here).
- `.gitignore`, `LICENSE` — project housekeeping.

## Overview
This project composes multiple specialized agents:
- `outline_agent` — creates a structured outline (headline, intro hook, 3–5 sections with bullets).
- `writer_agent` — consumes the outline and produces a 200–300 word draft.
- `editor_agent` — polishes the draft to fix grammar and improve flow.
- `root_agent` — runs agents in sequence for end-to-end output.
- `runner` — executes the pipeline and includes debug/run helpers.

Separating responsibilities reduces hallucination by constraining each agent's task and allowing validation between steps.

## Requirements
- Python 3.10+
- API key for the model service (add to `.env` as `API_KEY=your_key_here`).

## Setup (Windows)
1. Create and activate a virtual environment:
   - python -m venv .venv
   - .venv\Scripts\activate
2. Install dependencies:
   - pip install -r requirements.txt
3. Add your API key to `.env`:
   - API_KEY=...

## Run
- Start the interactive CLI:
  - python main.py
- Enter a blog topic when prompted; enter `exit` to quit.

## Notes & tips
- Adjust model selection and retry parameters in `main.py`.
- Use the provided `run_debug`/runner helpers to trace intermediate outputs.
- Do not commit `.env` (it's ignored by `.gitignore`).

## License
MIT — see `LICENSE`.