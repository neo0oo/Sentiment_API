# Sentiment_API
FastAPI service for multilingual sentiment analysis using Hugging Face Transformers.

## Quick Start
```bash
#  local
pip install -r requirements.txt
uvicorn main:app --reload     # http://127.0.0.1:8000/docs

# docker
docker build -t sentiment-api .
docker run -p 8000:80 sentiment-api

## What this project does
- FastAPI API with two endpoints: `/analyze` (single) and `/analyze_batch` (batch).
- Uses Hugging Face pipeline: `tabularisai/multilingual-sentiment-analysis`.
- Returns `{ label, score }`. Interactive docs at `/docs`.

Going to add twitter API so tweets are analyzed. (work in progress).
