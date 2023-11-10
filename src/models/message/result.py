from pydantic import BaseModel, condecimal
from typing import Dict, List
from ..common.enums import LabelType

Probability = condecimal(ge=0, le=1)


class Result(BaseModel):
    id: str
    probabilities: Dict[LabelType, Probability]


class AnalyzeResult(BaseModel):
    messages: List[Result]
