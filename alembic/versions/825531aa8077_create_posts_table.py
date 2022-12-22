"""create posts table

Revision ID: 825531aa8077
Revises: 
Create Date: 2022-12-22 17:46:27.325911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '825531aa8077'
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
