from pydantic import BaseModel
from enum import Enum
from typing import List


class StatusEnum(str, Enum):
    active = "ACTIVE"
    closed = "CLOSED"
    bankrut = "BANKRUPT"


class Data(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: StatusEnum


class Meta(BaseModel):
    total: int
    limit: int
    offset: int


class CompaniesModel(BaseModel):
    data: List[Data]
    meta: Meta
