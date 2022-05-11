""" Application Entrypoint """
from typing import Optional

from fastapi import FastAPI

from controller.users import router


app = FastAPI()

app.include_router(router)
