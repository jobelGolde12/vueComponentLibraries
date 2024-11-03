from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserAccount(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
