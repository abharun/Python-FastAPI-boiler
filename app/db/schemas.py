from sqlalchemy import Column, String, Integer, Float
from app.db.dbconnect import Base


class InventorySchema(Base):
    __tablename__ = "UserInfo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    