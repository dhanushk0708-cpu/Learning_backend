"""add email to users

Revision ID: 4930660a28e1
Revises: 9e524ad7b3c0
Create Date: 2026-09-05 00:24:16.260857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4930660a28e1'
down_revision: Union[str, Sequence[str], None] = '9e524ad7b3c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("email", sa.String(length=255), nullable=True)
    )


def downgrade() -> None:
    op.drop_column("users", "email")