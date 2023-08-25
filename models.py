from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Landmark(Base):
    __tablename__ = 'landmarks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    visited = Column(Boolean, default=False)
   
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship('Country', backref='landmarks')
