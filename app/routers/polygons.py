from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()


@router.post("/polygons_create")
def create_polygon(polygon: schemas.PolygonCreate, db: Session = Depends(get_db)):
    return crud.create_polygon(db, polygon)


@router.get("/get_polygons")
def read_polygons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_polygons(db, skip=skip, limit=limit)


@router.get("/by_id_polygons/{polygon_id}")
def read_polygon(polygon_id: int, db: Session = Depends(get_db)):
    polygon = crud.get_polygon(db, polygon_id)
    if polygon is None:
        raise HTTPException(status_code=404, detail="Polygon not found")
    return polygon


@router.put("/polygons_updated/{polygon_id}")
def update_polygon(polygon_id: int, polygon: schemas.PolygonUpdate, db: Session = Depends(get_db)):
    return crud.update_polygon(db, polygon_id, polygon)


@router.delete("/polygons_delete/{polygon_id}")
def delete_polygon(polygon_id: int, db: Session = Depends(get_db)):
    polygon = crud.delete_polygon(db, polygon_id)
    if polygon is None:
        raise HTTPException(status_code=404, detail="Polygon not found")
    return polygon
