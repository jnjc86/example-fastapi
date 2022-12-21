"""add content column to posts table

Revision ID: bda18dd7fc74
Revises: 7745e208af3a
Create Date: 2022-12-20 15:56:05.268715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bda18dd7fc74'
down_revision = '7745e208af3a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
