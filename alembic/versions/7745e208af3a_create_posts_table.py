"""create posts table

Revision ID: 7745e208af3a
Revises: 
Create Date: 2022-12-20 15:32:17.804350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7745e208af3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True)
    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass

