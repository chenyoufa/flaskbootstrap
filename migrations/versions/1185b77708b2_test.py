"""test

Revision ID: 1185b77708b2
Revises: 8dedc70f1ff7
Create Date: 2020-12-15 16:10:08.590524

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1185b77708b2'
down_revision = '8dedc70f1ff7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('SysUsers', sa.Column('PositionId', sa.Integer(), nullable=True))
    op.drop_constraint('SysUsers_ibfk_2', 'SysUsers', type_='foreignkey')
    op.create_foreign_key(None, 'SysUsers', 'SysPosition', ['PositionId'], ['Id'])
    op.drop_column('SysUsers', 'PositionIds')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('SysUsers', sa.Column('PositionIds', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'SysUsers', type_='foreignkey')
    op.create_foreign_key('SysUsers_ibfk_2', 'SysUsers', 'SysPosition', ['PositionIds'], ['Id'])
    op.drop_column('SysUsers', 'PositionId')
    # ### end Alembic commands ###
