from pydantic import BaseModel
from typing import List


class Request(BaseModel):
    text: str
    id: str


class AnalyzeRequest(BaseModel):
    messages: List[Request]
