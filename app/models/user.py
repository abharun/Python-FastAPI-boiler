from pydantic import BaseModel

class UserMode(BaseModel):
    email: str
    username: str
    password: str