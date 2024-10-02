from sqlalchemy import Column, String, Integer
from app.db.dbconnect import Base


class UserSchema(Base):
    __tablename__ = "UserInfo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
