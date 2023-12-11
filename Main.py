from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Integer)
    reviews = relationship("Review", backref="reviewed_restaurant")

    @classmethod
    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    reviews = relationship("Review", backref="customer")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self, session):
        return session.query(Restaurant).join(Review).filter(Review.customer_id == self.id).order_by(Review.rating.desc()).first()

    def add_review(self, session, restaurant, rating):
        review = Review(customer_id=self.id, restaurant_id=restaurant.id, rating=rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, session, restaurant):
        session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).delete()
        session.commit()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    rating = Column(Integer)
    restaurant = relationship("Restaurant", backref="restaurant_reviews")

    def full_review(self):
        return f"Review: {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars."

engine = create_engine('sqlite:///CuisineConnect.db')
Base.metadata.create_all(engine)
