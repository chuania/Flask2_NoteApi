"""empty message

Revision ID: 6ff7a4ca0b33
Revises: d5e0e56e547b
Create Date: 2024-04-15 14:59:59.035337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ff7a4ca0b33'
down_revision = 'd5e0e56e547b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=32), server_default='simple_user', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('note_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note_model')
    op.drop_table('user_model')
    # ### end Alembic commands ###