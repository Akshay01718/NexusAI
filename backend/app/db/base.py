# Import all models here so that Base.metadata has them registered before
# being imported by Alembic or other database scripts.

from app.db.database import Base  # noqa: F401

# Import your models here as you create them:
# e.g.,
# from app.models.user import User  # noqa: F401
