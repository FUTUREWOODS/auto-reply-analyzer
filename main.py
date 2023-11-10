from fastapi import FastAPI, Depends
from src.models.message.request import AnalyzeRequest
from src.models.message.result import AnalyzeResult, Result
from src.modules.auth import verify_token
from src.modules.categorize import categorize

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/analyze", response_model=AnalyzeResult)
async def analyze(request: AnalyzeRequest, authorized: bool = Depends(verify_token)):
    return categorize(request)
