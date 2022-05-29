""" Model for Chart """

from typing import List
from pydantic import BaseModel


# General Chart Model
class ChartModel(BaseModel):
    name: str
    reportId: str
    desc: str
    type: str


# Line Chart
class LineBar(BaseModel):
    id: str
    dataField: str
    color: str


class LineData(ChartModel):
    xaxis: str
    lines: List[LineBar]
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


# Bar Chart
class BarData(ChartModel):
    xaxis: str
    bars: List[LineBar]
    accumulator: str
    stacked: bool


class BarChart(BarData):
    id: str
    collectionName: str
