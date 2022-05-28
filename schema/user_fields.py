""" Model for User """

from pydantic import BaseModel

class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str
