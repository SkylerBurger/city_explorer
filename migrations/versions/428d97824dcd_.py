"""empty message

Revision ID: 428d97824dcd
Revises: 
Create Date: 2019-07-17 16:19:25.818636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '428d97824dcd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search_query', sa.String(length=256), nullable=True),
    sa.Column('formatted_query', sa.String(length=256), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('search_query')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location')
    # ### end Alembic commands ###