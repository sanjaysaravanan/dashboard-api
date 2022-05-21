""" Model for Chart """

from pydantic import BaseModel


# General Chart Model
class ChartModel(BaseModel):
    name: str
    reportId: str
    desc: str


# Line Chart
class Line(BaseModel):
    id: str
    dataField: str
    color: str
    accumulator: str


class LineChart(ChartModel):
    type: str
    xaxis: str
    lines: list[Line]


class LineData(LineChart):
    id: str
    collectionName: str
