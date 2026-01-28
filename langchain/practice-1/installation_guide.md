# Installation Guide (macOS)

This guide walks you through setting up **Local LLaMA (Ollama) + LangChain + uv** on macOS.

---

## Prerequisites
- macOS (Apple Silicon or Intel)
- Homebrew installed
- Python 3.9+

Verify:

```bash
python3 --version  
brew --version  
```
---

## Step 1 — Install uv (Python Package Manager)
```bash
pip install uv
```
or

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify:
```bash
uv --version
```

## Step 2 — Install Ollama (Local LLM Runtime)

```bash
brew install ollama
```
Start Ollama as a background service:
```bash
brew services start ollama
```
Stop Ollama:
```bash
brew services stop ollama
```

Verify:
```bash
ollama --version  
curl http://localhost:11434  
```
You should see a response confirming Ollama is running.

---

## Step 3 — Download LLaMA Model
```bash 
ollama pull llama3
```
Test:
```bash
ollama run llama3

>>> hi 
Hi! It's nice to meet you. Is there something I can help you with or would you like to chat?

```

Exit the chat with:
```bash
/bye
```
---

## Step 4 — Initialize Python Project Using uv

From your project root:

```bash
uv init
```
This creates:
- pyproject.toml
- .venv/

---

## Step 5 — Install Dependencies

```bash
uv add langchain langchain-community ollama
```
This generates:
- uv.lock
- Updates pyproject.toml

---

## Step 6 — Run Your App

Create your entry file:

Example:
```bash
mkdir -p src  
touch src/main.py  
```
Run:
```bash
uv run python src/main.py

uv run uvicorn main:app --reload --app-dir src

uv run uvicorn src.main:app --reload 

```

### Running a Specific File Inside `src`

To run a specific Python file inside the `src` directory, navigate to the `src` folder and execute the module using the `-m` flag.

```bash
cd src
uv run python -m chunking_strategy.character_splitter
```
