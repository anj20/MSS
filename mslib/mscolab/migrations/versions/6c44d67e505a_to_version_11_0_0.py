"""to_version_11_0_0

Revision ID: 6c44d67e505a
Revises: 922e4d9c94e2
Create Date: 2025-02-05 00:44:29.932413

"""
from alembic import op
import sqlalchemy as sa
import mslib.mscolab.custom_migration_types as cu


# revision identifiers, used by Alembic.
revision = '6c44d67e505a'
down_revision = '922e4d9c94e2'
branch_labels = None
depends_on = None



def upgrade():
    op.alter_column('changes', 'version_name', existing_type=sa.String(255), nullable=True)
    op.alter_column('changes', 'comment', existing_type=sa.String(255), nullable=True)


def downgrade():
    op.alter_column('changes', 'version_name', existing_type=sa.String(255), nullable=False)
    op.alter_column('changes', 'comment', existing_type=sa.String(255), nullable=False)
