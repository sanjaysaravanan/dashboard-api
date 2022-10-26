""" Application Entrypoint """

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from controller import users, reports, charts

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(reports.router)
app.include_router(charts.router)
