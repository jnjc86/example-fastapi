"""add content column to posts table

Revision ID: 2bbe16644802
Revises: 825531aa8077
Create Date: 2022-12-22 17:52:27.747684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bbe16644802'
down_revision = '825531aa8077'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
