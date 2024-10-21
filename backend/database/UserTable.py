from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserAccount(Base):
    __tablename__ = 'user_account'

    id = Column(Integer,autoincrement=True,nullable=False)
    email = Column(String(255), primary_key=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')

