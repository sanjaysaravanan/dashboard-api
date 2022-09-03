""" Model for Report """

from pydantic import BaseModel


class ReportModel(BaseModel):
    name: str
    type: str
    description: str
