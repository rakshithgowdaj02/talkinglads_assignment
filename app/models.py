from sqlalchemy import Column, Integer, String
from app.database import Base
# from geoalchemy2 import Geometry

# Base = declarative_base()


class Point(Base):
    __tablename__ = "points"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(1000), index=True)
    location = Column(String(1000))


class Polygon(Base):
    __tablename__ = "polygons"
    id = Column(Integer,  primary_key=True, autoincrement=True, index=True)
    name = Column(String(1000), index=True)
    boundary = Column(String(1000))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(191), unique=True, nullable=False)  # Reduced to 191
    email = Column(String(255), unique=True, nullable=False)  # Reduced to 255
    hashed_password = Column(String(255), nullable=False)  # Reduced to 255
