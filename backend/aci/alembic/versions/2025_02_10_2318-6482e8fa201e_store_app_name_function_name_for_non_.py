"""store app_name/function_name for non foreign key fields

Revision ID: 6482e8fa201e
Revises: adcfaa729f61
Create Date: 2025-02-10 23:18:55.457877+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "6482e8fa201e"
down_revision: Union[str, None] = "adcfaa729f61"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "agents",
        "excluded_apps",
        existing_type=postgresql.ARRAY(sa.UUID()),
        type_=postgresql.ARRAY(sa.String(length=255)),
        existing_nullable=False,
    )
    op.alter_column(
        "agents",
        "excluded_functions",
        existing_type=postgresql.ARRAY(sa.UUID()),
        type_=postgresql.ARRAY(sa.String(length=255)),
        existing_nullable=False,
    )
    op.alter_column(
        "app_configurations",
        "enabled_functions",
        existing_type=postgresql.ARRAY(sa.UUID()),
        type_=postgresql.ARRAY(sa.String(length=255)),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "app_configurations",
        "enabled_functions",
        existing_type=postgresql.ARRAY(sa.String(length=255)),
        type_=postgresql.ARRAY(sa.UUID()),
        existing_nullable=False,
    )
    op.alter_column(
        "agents",
        "excluded_functions",
        existing_type=postgresql.ARRAY(sa.String(length=255)),
        type_=postgresql.ARRAY(sa.UUID()),
        existing_nullable=False,
    )
    op.alter_column(
        "agents",
        "excluded_apps",
        existing_type=postgresql.ARRAY(sa.String(length=255)),
        type_=postgresql.ARRAY(sa.UUID()),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
