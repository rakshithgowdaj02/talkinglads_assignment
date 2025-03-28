from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class PointUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[dict] = None  # GeoJSON format


class PolygonUpdate(BaseModel):
    name: Optional[str] = None
    boundary: Optional[dict] = None  # GeoJSON format


class Token(BaseModel):
    access_token: str
    token_type: str


class PointBase(BaseModel):
    name: str
    location: dict  # GeoJSON format


class PointCreate(PointBase):
    pass


class PointOut(PointBase):
    id: int

    class Config:
        from_attributes = True


class PolygonBase(BaseModel):
    name: str
    boundary: dict  # GeoJSON format


class PolygonCreate(PolygonBase):
    name: str
    boundary: str



class PolygonOut(PolygonBase):
    id: int

    class Config:
        from_attributes = True
