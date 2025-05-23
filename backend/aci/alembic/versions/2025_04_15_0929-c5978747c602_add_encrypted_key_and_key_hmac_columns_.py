"""Add encrypted_key and key_hmac columns for api_keys table

Revision ID: c5978747c602
Revises: bce2fbe6273b
Create Date: 2025-04-15 09:29:41.112876+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from aci.common.db.custom_sql_types import Key

# revision identifiers, used by Alembic.
revision: str = 'c5978747c602'
down_revision: Union[str, None] = 'bce2fbe6273b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_keys', sa.Column('encrypted_key', Key(), nullable=True))
    op.add_column('api_keys', sa.Column('key_hmac', sa.String(length=64), nullable=True))
    op.create_unique_constraint('api_keys_encrypted_key_key', 'api_keys', ['encrypted_key'])
    op.create_unique_constraint('api_keys_key_hmac_key', 'api_keys', ['key_hmac'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('api_keys_encrypted_key_key', 'api_keys', type_='unique')
    op.drop_constraint('api_keys_key_hmac_key', 'api_keys', type_='unique')
    op.drop_column('api_keys', 'key_hmac')
    op.drop_column('api_keys', 'encrypted_key')
    # ### end Alembic commands ###
