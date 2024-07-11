"""Rename column user_tg_id -> tg_id

Revision ID: 9e7d4d5f3eb5
Revises: 1f162e4c8fce
Create Date: 2024-07-11 12:24:01.385309+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9e7d4d5f3eb5"
down_revision: Union[str, None] = "1f162e4c8fce"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("tg_id", sa.Integer(), nullable=False))
    op.drop_index("ix_users_user_tg_id", table_name="users")
    op.create_index(op.f("ix_users_tg_id"), "users", ["tg_id"], unique=True)
    op.drop_column("users", "user_tg_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "user_tg_id", sa.INTEGER(), autoincrement=True, nullable=False
        ),
    )
    op.drop_index(op.f("ix_users_tg_id"), table_name="users")
    op.create_index(
        "ix_users_user_tg_id", "users", ["user_tg_id"], unique=True
    )
    op.drop_column("users", "tg_id")
    # ### end Alembic commands ###