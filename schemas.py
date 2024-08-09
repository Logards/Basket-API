from pydantic import BaseModel


class UserSchema(BaseModel):
    email: str
    password: str


class UserConnectSchema(BaseModel):
    email: str
    password: str
