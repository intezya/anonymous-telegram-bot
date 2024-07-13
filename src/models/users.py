from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base
from schemas.user import UserSchema


class Users(Base):
    id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        primary_key=True,
        nullable=False,
        index=True,
    )
    hashed_id: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            hashed_id=self.hashed_id,
        )
