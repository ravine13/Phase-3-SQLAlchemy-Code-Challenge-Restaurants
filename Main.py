from sqlalchemy import Column, Integer, String, ForeignKey,create_engine
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))  
    price = Column(Integer)
    reviews = relationship("Review", backref="restaurant")

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))  
    reviews = relationship("Review", backref="customer")

  

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer = relationship("Customer", backref="reviews")
    restaurant = relationship("Restaurant", backref="reviews")
