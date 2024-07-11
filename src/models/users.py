import uuid

from sqlalchemy import BigInteger, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base
from schemas.user import UserSchema


class Users(Base):
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=uuid.uuid4,
    )
    tg_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        primary_key=True,
        nullable=False,
        index=True,
    )
    hashed_tg_id: Mapped[int] = mapped_column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            tg_id=self.tg_id,
            hashed_tg_id=self.hashed_tg_id,
        )
