"""add last few columns to posts table

Revision ID: 051d37fff79f
Revises: 17a548232cdb
Create Date: 2022-12-20 17:22:42.358141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051d37fff79f'
down_revision = '17a548232cdb'
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
