from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class SuperHero(Base):

    __tablename__ = 'superheroes'

    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    power = Column(String())