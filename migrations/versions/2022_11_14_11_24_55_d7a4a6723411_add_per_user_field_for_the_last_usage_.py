"""Add per-user field for the last usage of the Volunteer page

Revision ID: d7a4a6723411
Revises: b23ec080ecb7
Create Date: 2022-11-14 11:24:55.304258+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7a4a6723411'
down_revision = 'b23ec080ecb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('volunteer_last_started_utc', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'volunteer_last_started_utc')
    # ### end Alembic commands ###
