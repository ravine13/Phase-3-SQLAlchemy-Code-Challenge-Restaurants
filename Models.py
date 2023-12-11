from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Main import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///CuisineConnect.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



reviews = session.query(Review).all()


for review in reviews:
    print(review) 


session.close()