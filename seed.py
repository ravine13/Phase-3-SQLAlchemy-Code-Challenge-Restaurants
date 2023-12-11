from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Main import Base, Restaurant, Customer, Review
from faker import Faker

engine = create_engine('sqlite:///CuisineConnect.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

for _ in range(10):
    restaurant = Restaurant(
        name=fake.company(),
        price=fake.random_int(min=1, max=5)
    )
    session.add(restaurant)

for _ in range(20):
    customer = Customer(
        first_name=fake.first_name(),
        last_name=fake.last_name()
    )
    session.add(customer)

session.commit()

for restaurant in session.query(Restaurant).all():
    for customer in session.query(Customer).all():
        rating = fake.random_int(min=1, max=5)
        customer.add_review(session, restaurant, rating)

session.commit()


