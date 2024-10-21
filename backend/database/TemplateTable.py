from sqlalchemy import Column, Integer, String, TIMESTAMP, LargeBinary, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class TemplateTbl(Base):
    __tablename__ = 'template_tbl'

    id = Column(Integer, autoincrement=True, nullable=False)
    template_title = Column(String(255), nullable=False, primary_key=True)
    file_data = Column(LargeBinary)
    stored_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    download_counts = relationship("Downloads", back_populates="template")
    like_counts = relationship("Likes", back_populates="template")

class Downloads(Base):
    __tablename__ = 'download_counts'

    id = Column(Integer, autoincrement=True, nullable=False,primary_key=True)
    template_title_fk = Column(String(255), ForeignKey('template_tbl.template_title'), nullable=False) 
    who_download = Column(String(255), nullable=False)

    template = relationship("TemplateTbl", back_populates="download_counts")

class Likes(Base):
    __tablename__ = 'like_counts'

    id = Column(Integer, autoincrement=True, nullable=False,primary_key=True)
    template_title_fk = Column(String(255), ForeignKey('template_tbl.template_title'), nullable=False)  
    who_like = Column(String(255), nullable=False)

    template = relationship("TemplateTbl", back_populates="like_counts")
