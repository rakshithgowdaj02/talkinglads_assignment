from fastapi import FastAPI
from app.routers import polygons, points, auth
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Spatial Backend", description="API for managing users, points, and polygons with MySQL Spatial support")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(polygons.router, prefix="/polygons", tags=["Polygons"])
app.include_router(points.router, prefix="/points", tags=["Points"])

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Spatial Backend"}