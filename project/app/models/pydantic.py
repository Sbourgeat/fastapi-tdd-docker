#project/app/models/pydantic.py

from pydantic import BaseModel 

class SummaryPayloadSchema(BaseModel):
    """
    Summary payload schema
    """
    url : str


class SummaryResponseSchema(BaseModel):
    id : int