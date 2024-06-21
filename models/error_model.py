from typing import List

from pydantic import BaseModel


class Detail(BaseModel):
    type: str
    loc: List[str]
    msg: str
    type: str
    input: str
    url: str


class ValidationErrorModel(BaseModel):
    detail: List[Detail]
