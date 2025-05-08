from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK
from database import sessionLocal
import model

from database import engine
from schema import createUser, userLogin
from crud import register_user, login_user

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/registration', status_code = HTTP_201_CREATED)
def registration(data: createUser, db: Session = Depends(get_db)):
    user = register_user(data, db)
    if not user:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail = "Registration is Failed.")
    return {
        'status': 'Success',
        'message': 'Registration is Done.',
        'user': user,
    }

@app.post('/login', status_code=HTTP_200_OK)
def login(data: userLogin, db: Session = Depends(get_db)):
    user = login_user(data, db)
    if not user:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail = "Login is Failed.")
    return {
        'status': 'Success',
        'message': 'Login is Done.',
        'user': user
    }