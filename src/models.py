import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    registration_date = Column(DateTime, nullable=False)

    favorites = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet")
    character = relationship("Character")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    diameter = Column(Integer)
    climate = Column(String(50))
    population = Column(Integer)
    terrain = Column(String(100))

    favorites = relationship("Favorite", backref="planet")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(20))
    height = Column(Integer)
    weight = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))

    favorites = relationship("Favorite", backref="character")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e