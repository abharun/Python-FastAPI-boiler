from app.db.dbconnect import SessionLocal
from app.db.schemas import UserSchema
from app.models.user import UserModel
from sqlalchemy import and_
import hashlib

dbHandler = SessionLocal()


async def get_single_user(id: int):
    return dbHandler.query(UserSchema).filter(UserSchema.id == id).first()


async def auth_user(email: str, password: str):
    try:
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        exist_user = dbHandler.query(UserSchema).filter(UserSchema.email == email).first()
        return exist_user.password == password_hash
    except Exception as e:
        return False


async def get_multi_users(page: int, perpage: int):
    offset = (page - 1) * perpage
    return dbHandler.query(UserSchema).offset(offset).limit(perpage).all()


async def insert_user(user_info: UserModel):
    try :
        password_hash = hashlib.sha256(user_info.password.encode('utf-8')).hexdigest()
        new_user = UserSchema(
            email=user_info.email,
            username=user_info.username,
            password=password_hash,
        )
        dbHandler.add(new_user)
        dbHandler.commit()
        return True
    except Exception as e:
        return False


async def delete_user(id: int):
    try:
        user = dbHandler.query(UserSchema).filter(UserSchema.id == id).first()
        if user:
            dbHandler.delete(user)
            dbHandler.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
