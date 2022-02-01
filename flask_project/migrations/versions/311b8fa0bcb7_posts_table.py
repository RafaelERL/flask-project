"""posts table

Revision ID: 311b8fa0bcb7
Revises: 566306ff4cfb
Create Date: 2022-01-31 19:13:23.868994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '311b8fa0bcb7'
down_revision = '566306ff4cfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=160), nullable=True),
    sa.Column('category', sa.String(length=160), nullable=True),
    sa.Column('place', sa.String(length=160), nullable=True),
    sa.Column('address', sa.String(length=160), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('timestamp_end', sa.DateTime(), nullable=True),
    sa.Column('method', sa.String(length=160), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_index(op.f('ix_post_timestamp_end'), 'post', ['timestamp_end'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp_end'), table_name='post')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
