""" Graph generation Endpoint """

from fastapi import File, APIRouter, UploadFile

from schema.reports import ReportModel
from service.reports import Reports

router = APIRouter(
    prefix="/reports",
    tags=["reports"],
)

@router.post("/")
async def post(file: UploadFile = File(...)):
    """ Return file location to Service """
    contents = await file.read()
    return Reports().file_to_dataframe(contents)
    # return { "fileName": file.filename }
