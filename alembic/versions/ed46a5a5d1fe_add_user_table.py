"""add user table

Revision ID: ed46a5a5d1fe
Revises: bda18dd7fc74
Create Date: 2022-12-20 16:45:55.976899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed46a5a5d1fe'
down_revision = 'bda18dd7fc74'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                       sa.Column('id', sa.INTEGER(), nullable=False),
                       sa.Column('email', sa.String(), nullable=False),
                       sa.Column('password', sa.String(), nullable=False),
                       sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                       server_default=sa.text('now()'), nullable=False),
                       sa.PrimaryKeyConstraint('id'),
                       sa.UniqueConstraint('email')
                       )
    pass


def downgrade():
    op.drop_table('users')
    pass
