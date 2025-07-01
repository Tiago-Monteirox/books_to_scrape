from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scraper.models import Base

engine = create_engine("sqlite:///books.db")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)