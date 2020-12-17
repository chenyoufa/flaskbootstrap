"""test

Revision ID: 8dedc70f1ff7
Revises: d81887a96382
Create Date: 2020-12-15 16:08:57.748481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dedc70f1ff7'
down_revision = 'd81887a96382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('SysUsers', sa.Column('DepartmentId', sa.Integer(), nullable=True))
    op.add_column('SysUsers', sa.Column('PositionIds', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'SysUsers', 'SysDepartment', ['DepartmentId'], ['Id'])
    op.create_foreign_key(None, 'SysUsers', 'SysPosition', ['PositionIds'], ['Id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'SysUsers', type_='foreignkey')
    op.drop_constraint(None, 'SysUsers', type_='foreignkey')
    op.drop_column('SysUsers', 'PositionIds')
    op.drop_column('SysUsers', 'DepartmentId')
    # ### end Alembic commands ###