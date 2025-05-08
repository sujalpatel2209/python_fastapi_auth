from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from model import User
from schema import createUser, userLogin
from hash_password import hash_pwd, verify_password

def register_user(data: createUser, db: Session):
    user = User(
        name = data.name,
        username = data.username,
        password = hash_pwd(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(data: userLogin, db: Session):
    userDetail = db.query(User).filter(User.username == data.username).first()

    if not userDetail or not verify_password(data.password, userDetail.password):
        raise HTTPException(status_code = HTTP_401_UNAUTHORIZED, detail = 'Invalid username and password.')

    return userDetail

