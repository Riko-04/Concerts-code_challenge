"""Create concerts table

Revision ID: cedf15ef1b77
Revises: b01979c7ce45
Create Date: 2024-06-10 18:12:38.431687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cedf15ef1b77'
down_revision = 'b01979c7ce45'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'concerts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.String, nullable=False),
        sa.Column('band_id', sa.Integer, sa.ForeignKey('bands.id'), nullable=False),
        sa.Column('venue_id', sa.Integer, sa.ForeignKey('venues.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('concerts')
