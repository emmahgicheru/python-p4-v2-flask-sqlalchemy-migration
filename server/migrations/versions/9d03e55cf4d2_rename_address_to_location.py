"""rename address to location

Revision ID: 9d03e55cf4d2
Revises: b789f4d3dfa7
Create Date: 2025-08-29 15:33:56.838158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d03e55cf4d2'
down_revision = 'b789f4d3dfa7'
branch_labels = None
depends_on = None


def upgrade():
    # Rename the column without dropping data
    op.alter_column(
        'departments',
        'address',
        new_column_name='location',
        existing_type=sa.String(),
        existing_nullable=True,  # keep true during rename to avoid NOT NULL issues
    )

def downgrade():
    # Revert the rename
    op.alter_column(
        'departments',
        'location',
        new_column_name='address',
        existing_type=sa.String(),
        existing_nullable=True,
    )
