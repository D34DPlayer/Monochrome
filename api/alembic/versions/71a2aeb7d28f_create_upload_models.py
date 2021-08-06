"""Create upload models

Revision ID: 71a2aeb7d28f
Revises: 31080335cd7b
Create Date: 2021-08-01 20:44:20.308157

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '71a2aeb7d28f'
down_revision = '31080335cd7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uploadsession',
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('manga_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['manga_id'], ['manga.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('uploadedblob',
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('session_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['session_id'], ['uploadsession.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('uploadedblob')
    op.drop_table('uploadsession')
    # ### end Alembic commands ###