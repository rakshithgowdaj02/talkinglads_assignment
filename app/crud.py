from sqlalchemy.orm import Session
from app import schemas, models


async def create_point(db: Session, point: schemas.PointCreate):
    db_point = models.Point(name=point.name, location=point.location)
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point


async def get_points(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Point).offset(skip).limit(limit).all()


async def get_point(db: Session, point_id: int):
    return db.query(models.Point).filter(models.Point.id == point_id).first()


async def update_point(db: Session, point_id: int, point: schemas.PointUpdate):
    db_point = db.query(models.Point).filter(models.Point.id == point_id).first()
    if db_point:
        db_point.name = point.name
        db_point.location = point.location
        db.commit()
        db.refresh(db_point)
    return db_point


async def delete_point(db: Session, point_id: int):
    db_point = db.query(models.Point).filter(models.Point.id == point_id).first()
    if db_point:
        db.delete(db_point)
        db.commit()
    return db_point


async def create_polygon(db: Session, polygon: schemas.PolygonCreate):
    db_polygon = models.Polygon(name=polygon.name, boundary=polygon.boundary)
    db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return db_polygon


async def get_polygons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Polygon).offset(skip).limit(limit).all()


async def get_polygon(db: Session, polygon_id: int):
    return db.query(models.Polygon).filter(models.Polygon.id == polygon_id).first()


async def update_polygon(db: Session, polygon_id: int, polygon: schemas.PolygonUpdate):
    db_polygon = db.query(models.Polygon).filter(models.Polygon.id == polygon_id).first()
    if db_polygon:
        db_polygon.name = polygon.name
        db_polygon.boundary = polygon.boundary
        db.commit()
        db.refresh(db_polygon)
    return db_polygon


async def delete_polygon(db: Session, polygon_id: int):
    db_polygon = db.query(models.Polygon).filter(models.Polygon.id == polygon_id).first()
    if db_polygon:
        db.delete(db_polygon)
        db.commit()
    return db_polygon
