"""Users: tg_id: int -> bigint, hashed_tg_id: int -> string

Revision ID: b7a95e6f55ea
Revises: 9e7d4d5f3eb5
Create Date: 2024-07-11 12:32:12.937736+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b7a95e6f55ea"
down_revision: Union[str, None] = "9e7d4d5f3eb5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "tg_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
        autoincrement=True,
    )
    op.alter_column(
        "users",
        "hashed_tg_id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "hashed_tg_id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "users",
        "tg_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        autoincrement=True,
    )
    # ### end Alembic commands ###
