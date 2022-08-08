import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    nickname = Column(String(250), nullable=False)


class character(Base):
    __tablename__ = 'character'
  
    id = Column(Integer, primary_key=True)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    affiliation = Column(String(250), nullable=True)
    light_saber = Column(String(250), nullable=True)

class planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surface = Column(Integer, nullable=False)

class starship(Base):
    __tablename__ = 'starship'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    guns = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    affiliation = Column(String(250), nullable=True)

class faction(Base):
    __tablename__ = 'faction'
    
    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)

class favourite(Base):
    __tablename__='favourite'

    id = Column(Integer,primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    character = Column(Integer, ForeignKey('character.id'))
    planet = Column(Integer, ForeignKey('planet.id'))
    starship = Column(Integer, ForeignKey('starship.id'))
    affiliation = Column(Integer, ForeignKey('faction.id'))

  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')