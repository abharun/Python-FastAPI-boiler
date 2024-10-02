from app.db.dbconnect import SessionLocal
from app.db.schemas import UserSchema
from app.models.user import UserModel
from sqlalchemy import and_
import hashlib

dbHandler = SessionLocal()


async def get_single_user(id: int):
    return await dbHandler.query(UserSchema).filter(UserSchema.id == id).first()


async def auth_user(email: str, password: str):
    crypted = hashlib.sha256(password)
    exist_user = await dbHandler.query(UserSchema).filter(
        and_(UserSchema.email == email, UserSchema.password == crypted)
    )
    return exist_user is not None


async def get_multi_users(page: int, perpage: int):
    offset = (page - 1) * perpage
    return await dbHandler.query(UserSchema).offset(offset).limit(perpage).all()


async def insert_user(user_info: UserModel):
    new_user = UserSchema(
        email=user_info.email,
        username=user_info.username,
        password=hashlib.sha256(user_info.password),
    )
    dbHandler.add(new_user)
    dbHandler.commit()


async def delete_user(id: int):
    user = await dbHandler.query(UserSchema).filter(UserSchema.id == id).first()

    if user:
        dbHandler.delete(user)
        dbHandler.commit()
        return True
    else:
        return False
