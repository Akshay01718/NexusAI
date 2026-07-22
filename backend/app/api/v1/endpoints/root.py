from fastapi import APIRouter
from sqlalchemy import text
from app.db.session import engine
router = APIRouter()

@router.get("/db-test")
def test_database():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        version = result.scalar()

    return {
        "status": "Connected!",
        "database": version,
    }