# 📝 Multiagent Blog Writer

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Google Gemini API](https://img.shields.io/badge/powered_by-Google_Gemini-orange)](https://ai.google.dev/)

> **Intelligent multi-agent blog content generation** — Reduce hallucination and improve output quality by splitting the writing process across specialized agents.

## 🎯 What is this?

This project demonstrates how **multiple AI agents can work together** to produce higher-quality blog posts. By dividing the writing task into discrete steps (outline → draft → edit), each agent focuses on a specific responsibility, reducing errors and hallucinations.

```
Topic Input → Outline Agent → Writer Agent → Editor Agent → Polished Blog Post
```

## ✨ Key Features

- 🤖 **Multi-Agent Pipeline** — Specialized agents for different writing stages
- 🎯 **Reduced Hallucination** — Task separation and validation between steps
- ⚡ **Async Processing** — Fast, concurrent execution using Google Gemini API
- 🔧 **Configurable** — Easy to adjust models, retry logic, and prompts
- 💬 **Interactive CLI** — Simple command-line interface for generating blog posts

## 🏗️ Architecture

| Agent | Responsibility |
|-------|-----------------|
| **Outline Agent** | Creates structured outlines (headline, intro, 3-5 sections with bullets) |
| **Writer Agent** | Drafts 200-300 word blog posts from outlines |
| **Editor Agent** | Polishes drafts for grammar, flow, and readability |
| **Root Agent** | Orchestrates the full pipeline end-to-end |
| **Runner** | Executes the pipeline with debug capabilities |

## 📋 Project Structure

```
multiagent-blog-writer/
├── main.py                 # Pipeline & entrypoint (async def main())
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (add API_KEY here)
├── .gitignore             # Git exclusions
├── LICENSE                # MIT License
└── README.md              # This file
```

## 🛠️ Requirements

- **Python 3.10+**
- **Google Gemini API Key** ([Get one here](https://ai.google.dev/))

## 🚀 Quick Start

### 1️⃣ Setup (Windows)

```powershell
# Create virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Configure

Create a `.env` file in the project root:

```env
API_KEY=your_gemini_api_key_here
```

> ⚠️ **Never commit `.env` to version control** — it's already in `.gitignore`

### 3️⃣ Run

```powershell
python main.py
```

Enter a blog topic when prompted. Type `exit` to quit.

**Example:**
```
Enter blog topic: The Future of AI in Education
→ Generates outline → draft → polished blog post
```

## 🔧 Customization

**In `main.py`, you can:**

- 🤖 Change model: `model="gemini-2.5-flash-lite"` → other Gemini models
- 🔄 Adjust retry logic: Modify `retry_config` settings
- ✏️ Customize agent instructions: Edit `instruction` parameters
- 📊 Trace intermediate outputs: Use `run_debug`/runner helpers

## 📚 How It Works

1. **Outline** — Agent generates a structured outline based on the topic
2. **Draft** — Writer creates a 200-300 word post following the outline
3. **Edit** — Editor refines for grammar, flow, and quality
4. **Output** — Final polished blog post ready to use

This multi-step approach significantly reduces hallucination compared to single-agent generation.

## 💡 Tips & Best Practices

- Start with the interactive CLI (`python main.py`) to see the full pipeline
- Use provided debugging helpers to inspect intermediate outputs
- Experiment with different topics to see how the agents adapt
- Monitor API usage in your Google Cloud Console

## 📄 License

MIT — See [LICENSE](LICENSE) for details.

