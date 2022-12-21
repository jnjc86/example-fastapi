"""add content column to posts table

Revision ID: e7460112323e
Revises: 051d37fff79f
Create Date: 2022-12-20 17:53:07.501014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7460112323e'
down_revision = '051d37fff79f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

