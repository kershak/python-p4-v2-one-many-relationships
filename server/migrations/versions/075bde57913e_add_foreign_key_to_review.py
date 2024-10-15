"""add foreign key to Review

Revision ID: 075bde57913e
Revises: 8ca3900fa7c2
Create Date: 2024-10-12 11:43:46.789378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '075bde57913e'
down_revision = '8ca3900fa7c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
