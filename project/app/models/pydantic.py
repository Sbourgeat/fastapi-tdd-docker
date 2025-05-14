# project/app/models/pydantic.py

from pydantic import AnyHttpUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl


class SummaryResponseSchema(BaseModel):
    id: int
    url: AnyHttpUrl


class SummaryUpdatePayloadSchema(BaseModel):
    url: AnyHttpUrl
    summary: str
