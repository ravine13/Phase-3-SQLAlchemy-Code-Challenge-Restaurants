from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Main import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///CuisineConnect.db')


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


restaurant = session.query(Restaurant).first() 
reviews = restaurant.all_reviews()

for review in reviews:
    print(review)
session.close()
