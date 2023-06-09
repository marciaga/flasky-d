"""Make pet_count nullable

Revision ID: 93a28783c745
Revises: 434c6e2c7e6c
Create Date: 2022-12-14 12:16:03.671384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93a28783c745'
down_revision = '434c6e2c7e6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cat', 'pet_count',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cat', 'pet_count',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
