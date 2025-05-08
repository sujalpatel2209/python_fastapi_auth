from pydantic import BaseModel


class createUser(BaseModel):
    name: str
    username: str
    password: str

class userLogin(BaseModel):
    username: str
    password: str