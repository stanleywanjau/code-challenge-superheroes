"""added relationships

Revision ID: 7884d14132d3
Revises: 8c767f18e001
Create Date: 2024-01-28 15:33:14.844563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7884d14132d3'
down_revision = '8c767f18e001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_hero_powers_power_id_powers'), 'powers', ['power_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_hero_powers_hero_id_heroes'), 'heroes', ['hero_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_hero_powers_hero_id_heroes'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_hero_powers_power_id_powers'), type_='foreignkey')

    # ### end Alembic commands ###
