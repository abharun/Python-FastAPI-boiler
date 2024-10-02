from fastapi import APIRouter, Query

from app.models.user import UserModel
from app.services import UserService

user_api = APIRouter()


@user_api.get("/{id}")
async def get_user_with_id(id: int):
    return await UserService.get_single_user(id=id)


@user_api.get("/")
async def get_user_for_page(page: int = Query(1, ge=1), perpage: int = Query(10, ge=5)):
    return await UserService.get_multi_users(page=page, perpage=perpage)


@user_api.post("/signup")
async def sign_up_user(new_user: UserModel):
    result = await UserService.insert_user(new_user)
    if result:
        return {"Status": "Success"}
    else:
        return {"Status": "Failed"}


@user_api.post("/signin")
async def sign_in_user(user: UserModel):
    result = await UserService.auth_user(email=user.email, password=user.password)
    if result:
        return {"Status": "Success"}
    else:
        return {"Status": "Failed"}


@user_api.delete("/")
async def delete_user(id: int):
    result = await UserService.delete_user(id=id)
    if result:
        return {"Status": "Success"}
    else:
        return {"Status": "Failed"}
