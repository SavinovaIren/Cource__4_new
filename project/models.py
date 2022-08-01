from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey(Genre.id))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey(Director.id))
    director = relationship("Director")


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favourite_genre = Column(ForeignKey(Genre.id))
    genre = relationship("Genre")

