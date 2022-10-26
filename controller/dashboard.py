""" Dashboard Endpoints """

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from schema.dashboard import DashboardModel
from service.dashboard import Dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"],
)


@router.get("")
async def get():
    """ Return the dashboard """
    return Dashboard().get_dashboard()

@router.post("")
async def save_dashboard(dashboard: DashboardModel):
    """ saves dashabord """
    data = jsonable_encoder(dashboard)
    return Dashboard().save_dashboard(data)
