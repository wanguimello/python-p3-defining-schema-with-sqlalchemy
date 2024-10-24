#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()

#creating the table
# Define your data model as a class
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())


if __name__ == '__main__':
    #persisting/saving the table
    # Create a SQLite database engine
    engine = create_engine('sqlite:///students.db')
    # Create the database schema
    Base.metadata.create_all(engine)
