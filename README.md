# Phase-3-SQLAlchemy-Code-Challenge-Restaurants

# CuisineConnect Database
Overview
The CuisineConnect Database is a project designed to manage restaurants, customers, and reviews using SQLAlchemy, allowing for relationships between customers, restaurants, and their associated reviews.

# Files
main.py: Contains the SQLAlchemy model definitions for Restaurant, Customer, and Review.
seed.py: Seeds the database with sample data for restaurants, customers, and reviews.
README.md: This file - a guide to understand and run the project.
Setup
## Environment Setup:

Create a Python virtual environment.
Install dependencies using pip install -r requirements.txt.

## Database Setup:
Ensure you have an SQLite database named CuisineConnect.db.
Run python seed.py to seed the database with sample data.
Usage

## Running the Project:

Ensure the required environment is activated.
Execute python main.py to run the SQLAlchemy models.


# Customizing Data:
Modify the seed script or manually manipulate data in the database using the SQLAlchemy models.
Project Structure
Models: Contains SQLAlchemy model definitions for restaurants, customers, and reviews.
Seed Script: Seeds the database with initial data.
Additional Files: Any other files or modules associated with the project.
Contributing
Feel free to contribute by suggesting improvements, reporting issues, or adding features via pull requests.


# Dependencies
SQLAlchemy
Faker
Alembic (for managing database migrations)