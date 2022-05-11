""" Users Endpoint """

from fastapi import APIRouter

from schema.user_fields import User, LoginUser
from service.users import Users

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/login")
async def login_user(login_user: LoginUser):
    """ Login a user on valid credential """
    return Users().login_user(login_user)

@router.post("/create-user")
async def create_user(user: User):
        """ Creates a user """
        return Users().create_user(user)

@router.get("/{email}")
async def get(email):
    """ Return a user with email """
    return Users().get_user(email)

@router.delete("/{email}")
async def delete(self, email):
    """ Deletes a user with email """
    return Users().delete_user(email)
