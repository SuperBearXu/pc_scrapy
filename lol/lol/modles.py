# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    author = Column(String(255))
    tags = relationship("Tag", back_populates="article")

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(String(255))
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship("Article", back_populates="tags")

def db_connect():
    return create_engine('mysql+pymysql://your_username:your_password@localhost/your_database')

def create_tables(engine):
    Base.metadata.create_all(engine)
