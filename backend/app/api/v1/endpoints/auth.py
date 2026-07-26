from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse
from app.utils.security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

user_repository = UserRepository()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    if user_repository.get_by_email(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    if user_repository.get_by_username(db, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    password_hash = hash_password(user.password)

    new_user = user_repository.create(
        db=db,
        user=user,
        password_hash=password_hash,
    )

    return new_user