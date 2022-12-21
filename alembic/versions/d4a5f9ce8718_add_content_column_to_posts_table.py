"""add content column to posts table

Revision ID: d4a5f9ce8718
Revises: e7460112323e
Create Date: 2022-12-20 18:05:56.010586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4a5f9ce8718'
down_revision = 'e7460112323e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
