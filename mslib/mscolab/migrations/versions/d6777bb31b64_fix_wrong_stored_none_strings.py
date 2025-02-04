"""Fix wrong stored None strings

Revision ID: d6777bb31b64
Revises: 922e4d9c94e2
Create Date: 2025-02-04 22:46:11.605418

"""
from alembic import op
import sqlalchemy as sa
import mslib.mscolab.custom_migration_types as cu


# revision identifiers, used by Alembic.
revision = 'd6777bb31b64'
down_revision = '922e4d9c94e2'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('changes', 'version_name', existing_type=sa.String(255), nullable=True)
    op.alter_column('changes', 'comment', existing_type=sa.String(255), nullable=True)


def downgrade():
    op.alter_column('changes', 'version_name', existing_type=sa.String(255), nullable=False)
    op.alter_column('changes', 'comment', existing_type=sa.String(255), nullable=False)
