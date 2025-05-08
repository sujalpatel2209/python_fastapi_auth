from sqlalchemy import Column, Integer, String

from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(150))
    username = Column(String(150), unique = True)
    password = Column(String(512))