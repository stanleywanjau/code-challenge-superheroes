"""corrected tables

Revision ID: ad556c508988
Revises: 7884d14132d3
Create Date: 2024-01-28 16:08:24.918179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad556c508988'
down_revision = '7884d14132d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hero',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('super_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('power',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('heropower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(), nullable=True),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('power_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['hero.id'], name=op.f('fk_heropower_hero_id_hero')),
    sa.ForeignKeyConstraint(['power_id'], ['power.id'], name=op.f('fk_heropower_power_id_power')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('heroes')
    op.drop_table('hero_powers')
    op.drop_table('powers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('powers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('update_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero_powers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('strength', sa.VARCHAR(), nullable=True),
    sa.Column('power_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('update_at', sa.DATETIME(), nullable=True),
    sa.Column('hero_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], name='fk_hero_powers_hero_id_heroes'),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], name='fk_hero_powers_power_id_powers'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('heroes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('super_name', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('update_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('heropower')
    op.drop_table('power')
    op.drop_table('hero')
    # ### end Alembic commands ###
