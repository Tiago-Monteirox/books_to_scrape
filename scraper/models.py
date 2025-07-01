from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    preco = Column(String)
    link = Column(String, unique=True)