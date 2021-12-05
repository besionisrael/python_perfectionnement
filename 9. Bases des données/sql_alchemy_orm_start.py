
#create db houshold
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


#engine

#ORM side with object relational mapping. This will make interacting with our 
# database more Pythonic. All models in SQLAlchemy are based on the declarative base


#create class/table


# we can create all of the corresponding tables in SQL with base.metadata.create all and pass in the engine.


#creating a project


#bulk save


#retrieving data
