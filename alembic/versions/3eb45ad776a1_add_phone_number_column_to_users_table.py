"""add phone_number column to users table

Revision ID: 3eb45ad776a1
Revises: c345d73ca98b
Create Date: 2026-01-05 19:16:06.510253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3eb45ad776a1'
down_revision: Union[str, Sequence[str], None] = 'c345d73ca98b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
