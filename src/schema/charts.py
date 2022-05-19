""" Model for Chart """

from pydantic import BaseModel

class ChartModel(BaseModel):
    name: str
    reportId: str
    description: str


class Line(BaseModel):
    id: str
    dataField: str
    color: str
    accumulator: str


class LineChart(ChartModel):
    type: str
    xaxis: str
    lines: list[Line]
