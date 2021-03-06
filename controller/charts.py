""" Charts Endpoint """

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from schema.charts import LineChart, LineData, PieChart, \
    PieData, BarChart, BarData
from service.charts import Charts

router = APIRouter(
    prefix="/charts",
    tags=["charts"],
)

@router.get("")
async def get_all_charts():
    """ Get all Charts """

    return Charts().get_all()

# Line Chart
@router.post("/line")
async def create_line_chart(line_data: LineData):
    """ Create new line Chart """

    data = jsonable_encoder(line_data)

    return Charts().save_line_chart(data)


@router.post("/line/data")
async def get_line_data(line_chart: LineChart):
    """ Retuns Line Chart data """

    data = jsonable_encoder(line_chart)

    return Charts().data_line_chart(data)


# Pie Chart
@router.post("/pie")
async def create_pie_chart(pie_data: PieData):
    """ Create new Pie Chart """

    data = jsonable_encoder(pie_data)

    return Charts().save_pie_chart(data)


@router.post("/pie/data")
async def get_pie_data(pie_chart: PieChart):
    """ Retuns Pie Chart data """

    data = jsonable_encoder(pie_chart)

    return Charts().data_pie_chart(data)


# Bar Chart
@router.post("/bar")
async def create_pie_chart(bar_data: BarData):
    """ Create new Bar Chart """

    data = jsonable_encoder(bar_data)

    return Charts().save_line_chart(data)


@router.post("/bar/data")
async def get_bar_data(bar_chart: BarChart):
    """ Retuns Pie Chart data """

    data = jsonable_encoder(bar_chart)

    return Charts().data_bar_chart(data)


@router.delete("/{chart_id}")
async def delete_chart(chart_id):
    """ Delete One Chart """
    return Charts().delete_one(chart_id)


@router.get("/data/{chart_id}")
async def get_chart_data(chart_id):
    """ Get Chart Data """
    return Charts().get_chart_data(chart_id)
