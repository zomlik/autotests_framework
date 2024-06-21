from pydantic import BaseModel


class CreateUserModel(BaseModel):
    first_name: str
    last_name: str
    company_id: int


class ResponseUserModel(BaseModel):
    first_name: str
    last_name: str
    company_id: int
    user_id: int


class Reason(BaseModel):
    reason: str


class UserErrorModel(BaseModel):
    detail: Reason
