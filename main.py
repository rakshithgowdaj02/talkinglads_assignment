from fastapi import FastAPI
from app.routers import polygons, points, auth
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Spatial Backend",
              description="API for managing users, points, and polygons with MySQL Spatial support",
              docs_url="/talking_lands/docs", openapi_url="/talking_lands/openapi.json")

# Include routers
app.include_router(auth.router, prefix="/talking_lands/auth", tags=["Authentication"])
app.include_router(polygons.router, prefix="/talking_lands/polygons", tags=["Polygons"])
app.include_router(points.router, prefix="/talking_lands/points", tags=["Points"])


@app.get("/health_check", tags=["Health check"])
def root():
    return {"message": "Welcome to FastAPI Spatial Backend"}
