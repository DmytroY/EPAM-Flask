"""empty message

Revision ID: fd0e57557592
Revises: 
Create Date: 2023-02-20 22:43:22.379260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd0e57557592'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('grade', sa.String(length=30), nullable=True),
    sa.Column('specialization', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('health_state', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    op.drop_table('doctors')
    # ### end Alembic commands ###
