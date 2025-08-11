from pydantic import BaseModel
from enum import Enum
from typing import List


class AnalyzeRequest(BaseModel):
    text: str 

class AnalyzeResponse(BaseModel):
    label: str 
    score: float 

class BatchAnalyzeRequest(BaseModel):
    texts: List[str]

class BatchAnalyzeResponse(BaseModel):
    results: List[AnalyzeResponse]
