""" Graph generation Endpoint """

from fastapi import File, APIRouter, UploadFile, Form

from schema.reports import ReportModel
from service.reports import Reports

router = APIRouter(
    prefix="/reports",
    tags=["reports"],
)


@router.get("")
async def get():
    """ Return all the reports """
    return Reports().get_all()


@router.post("")
async def post(
    file: UploadFile = File(...),
    name: str = Form(...),
    desc: str = Form(...),
    type: str = Form(...)
):
    """ Return file location to Service """
    contents = await file.read()
    data = {
        'name': name,
        'desc': desc,
        'type': type
    }
    return Reports().file_to_dataframe(contents, data)


@router.delete("/{report_id}")
async def delete(report_id):
    """ Delete One Report """
    return Reports().delete_one(report_id)
