from pydantic import BaseModel
from typing import List


class Detail(BaseModel):
    type: str
    loc: List[str]
    msg: str
    type: str
    input: str
    url: str


class ErrorMessageModel(BaseModel):
    detail: List[Detail]


