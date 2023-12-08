from sqlalchemy import Column, Integer, String, ForeignKey,create_engine
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///CuisineConnect.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)