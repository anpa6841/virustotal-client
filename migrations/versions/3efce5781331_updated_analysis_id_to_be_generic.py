"""updated analysis id to be generic

Revision ID: 3efce5781331
Revises: 
Create Date: 2023-06-04 17:49:28.110239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3efce5781331'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('analysis', schema=None) as batch_op:
        batch_op.add_column(sa.Column('resource_id', sa.String(length=300), nullable=True))
        batch_op.create_unique_constraint('unique_resc_id', ['resource_id'])
        batch_op.drop_column('file_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('analysis', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_id', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('resource_id')

    # ### end Alembic commands ###