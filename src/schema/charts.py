""" Model for Chart """

from pydantic import BaseModel


# General Chart Model
class ChartModel(BaseModel):
    name: str
    reportId: str
    desc: str
    type: str


# Line Chart
class Line(BaseModel):
    id: str
    dataField: str
    color: str
    

class LineData(ChartModel):
    xaxis: str
    lines: list[Line]
    accumulator: str


class LineChart(LineData):
    id: str
    collectionName: str


# Pie Chart
class PieData(ChartModel):
    dataField: str
    showBy: str
    accumulator: str


class PieChart(PieData):
    id: str
    collectionName: str

