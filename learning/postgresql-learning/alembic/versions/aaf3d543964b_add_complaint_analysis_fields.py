"""add complaint analysis fields

Revision ID: aaf3d543964b
Revises: 4930660a28e1
Create Date: 2026-09-10 14:39:19.924343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aaf3d543964b'
down_revision: Union[str, Sequence[str], None] = '4930660a28e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade() -> None:
    op.add_column(
        "complaints",
        sa.Column("category", sa.String(length=100), nullable=True)
    )

    op.add_column(
        "complaints",
        sa.Column("priority", sa.String(length=50), nullable=True)
    )


def downgrade() -> None:
    op.drop_column("complaints", "priority")
    op.drop_column("complaints", "category")