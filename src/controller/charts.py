""" Charts Endpoint """

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from schema.charts import LineChart
from service.charts import Charts

router = APIRouter(
    prefix="/charts",
    tags=["charts"],
)


@router.post("/line")
async def create_line_chart(line_chart: LineChart):
    """ Create new line Chart """

    data = jsonable_encoder(line_chart)

    return Charts().save_chart(data)