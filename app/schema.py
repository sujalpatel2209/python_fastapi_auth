from pydantic import BaseModel


class createUser(BaseModel):
    name: str
    username: str
    password: str

class userLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str