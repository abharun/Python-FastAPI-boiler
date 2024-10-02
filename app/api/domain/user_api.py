from fastapi import APIRouter, Query

from app.models.user import UserModel

user_api = APIRouter()


@user_api.get("/{id}")
async def get_user_with_id(id: int):
    pass


@user_api.get("/")
async def get_user_for_page(page: int = Query(1, ge=1), perpage: int = Query(10, ge=5)):
    pass


@user_api.post("/signup")
async def sign_up_user(new_user: UserModel):
    pass


@user_api.post("/signin")
async def sign_in_user(new_user: UserModel):
    pass


@user_api.delete("/")
async def delete_user(id: int):
    pass
