"""add content column to posts table

Revision ID: 970b36f9f4e2
Revises: 93518ec0a352
Create Date: 2026-01-05 15:42:07.956656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '970b36f9f4e2'
down_revision: Union[str, Sequence[str], None] = '93518ec0a352'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
