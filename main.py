from fastapi import FastAPI, HTTPException
from transformers import pipeline 
from models import AnalyzeRequest, AnalyzeResponse, BatchAnalyzeRequest, BatchAnalyzeResponse

app = FastAPI(
    title="Setiment Analysis API",
    description="API for analyzing sentiment of text & returning sentiment score",
    version="1.0.0",
    debug=True
)

@app.on_event("startup")
async def load_model():
    app.state.classifier = pipeline("text-classification",model = "tabularisai/multilingual-sentiment-analysis")

@app.get("/")
async def root():
    return {"message": "Sentiment API is running! Visit /docs or POST to /analyze"}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    result = app.state.classifier(request.text)[0]
    return AnalyzeResponse(
        label = str(result["label"]),
        score=float(result["score"])
    )

@app.post("/batch-analyze", response_model=BatchAnalyzeResponse)
async def batch_analyze(request: BatchAnalyzeRequest):
    texts = [t for t in request.texts if isinstance(t, str) and t.strip()]
    if not texts:
        raise HTTPException(status_code=400, detail="texts must include at least one non_empty string")
    raw = app.state.classifier(texts)
    if raw and isinstance(raw[0], list):
        raw = [max(item, key=lambda x: x["score"]) for item in raw]
    results = [AnalyzeResponse(label=str(r["lavel"]), score=float(r["score"])) for r in raw]
    return BatchAnalyzeResponse(results=results)