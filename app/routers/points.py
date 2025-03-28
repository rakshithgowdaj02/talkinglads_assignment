from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()


@router.post("/")
def create_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    return crud.create_point(db, point)


@router.get("/")
def read_points(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_points(db, skip=skip, limit=limit)


@router.get("/{point_id}")
def read_point(point_id: int, db: Session = Depends(get_db)):
    point = crud.get_point(db, point_id)
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return point


@router.put("/{point_id}")
def update_point(point_id: int, point: schemas.PointUpdate, db: Session = Depends(get_db)):
    return crud.update_point(db, point_id, point)


@router.delete("/{point_id}")
def delete_point(point_id: int, db: Session = Depends(get_db)):
    point = crud.delete_point(db, point_id)
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return point
