""" Charts Endpoint """

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from schema.charts import LineChart, LineData
from service.charts import Charts

router = APIRouter(
    prefix="/charts",
    tags=["charts"],
)

@router.get("")
async def get_all_charts():
    """ Get all Charts """

    return Charts().get_all()

@router.post("/line")
async def create_line_chart(line_chart: LineChart):
    """ Create new line Chart """

    data = jsonable_encoder(line_chart)

    return Charts().save_line_chart(data)


@router.post("/line/data")
async def get_line_data(line_chart: LineData):
    """ Retuns Line Chart data """

    data = jsonable_encoder(line_chart)

    return Charts().data_line_chart(data)

@router.delete("/{chart_id}")
async def delete_chart(chart_id):
    """ Delete One Chart """
    return Charts().delete_one(chart_id)