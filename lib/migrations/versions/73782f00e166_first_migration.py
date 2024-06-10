"""First migration

Revision ID: 73782f00e166
Revises: 
Create Date: 2022-09-19 00:02:16.845927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73782f00e166'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'bands',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('hometown', sa.String(), nullable=True)
    )
    op.create_table(
        'venues',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('city', sa.String(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('venues')
    op.drop_table('bands')
