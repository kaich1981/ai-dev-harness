#!/bin/bash
# Quick start script for AI Stock Assistant
set -e

cd "$(dirname "$0")"

echo "==> Installing dependencies..."
pip install -r requirements.txt -q

echo "==> Running tests..."
python -m pytest tests/ -v

echo "==> Starting server at http://127.0.0.1:8000"
echo "==> API docs: http://127.0.0.1:8000/docs"
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
