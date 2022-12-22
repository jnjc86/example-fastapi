"""add foreign-key to posts table

Revision ID: 3418b92955e6
Revises: b8f240f747eb
Create Date: 2022-12-22 18:17:29.377263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3418b92955e6'
down_revision = 'b8f240f747eb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.INTEGER(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'],
     remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass

