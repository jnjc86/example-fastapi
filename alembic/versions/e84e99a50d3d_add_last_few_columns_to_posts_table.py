"""add last few columns to posts table

Revision ID: e84e99a50d3d
Revises: 3418b92955e6
Create Date: 2022-12-22 18:26:44.249822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e84e99a50d3d'
down_revision = '3418b92955e6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.BOOLEAN(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('create_at', sa.TIMESTAMP(timezone=True), 
    nullable=False, server_default=sa.text ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
