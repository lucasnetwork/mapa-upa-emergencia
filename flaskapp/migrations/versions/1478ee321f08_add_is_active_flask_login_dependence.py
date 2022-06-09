"""add is_active flask_login dependence

Revision ID: 1478ee321f08
Revises: 73d4cc2bae96
Create Date: 2022-06-09 21:22:00.624993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1478ee321f08'
down_revision = '73d4cc2bae96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###
