# -*- coding: utf-8 -*-
"""post ref for work_package

Revision ID: d24b37426857
Revises: 3358eb6834e6
Create Date: 2022-12-28 11:42:26.773704

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "d24b37426857"
down_revision = "3358eb6834e6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("post", sa.Column("depth", sa.Integer(), server_default=sa.text("0"), nullable=False))
    op.add_column("post", sa.Column("children_count", sa.Integer(), server_default=sa.text("0"), nullable=False))
    op.add_column("post_reaction", sa.Column("work_package_id", postgresql.UUID(as_uuid=True), nullable=False))
    op.drop_constraint("post_reaction_post_id_fkey", "post_reaction", type_="foreignkey")
    op.create_foreign_key(None, "post_reaction", "work_package", ["work_package_id"], ["id"])
    op.drop_column("post_reaction", "post_id")
    op.add_column("work_package", sa.Column("done", sa.Boolean(), server_default=sa.text("false"), nullable=False))
    op.add_column("work_package", sa.Column("ack", sa.Boolean(), nullable=True))
    op.add_column("work_package", sa.Column("frontend_ref_post_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column("work_package", sa.Column("thread_id", sqlmodel.sql.sqltypes.GUID(), nullable=True))
    op.add_column("work_package", sa.Column("parent_post_id", sqlmodel.sql.sqltypes.GUID(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("work_package", "parent_post_id")
    op.drop_column("work_package", "thread_id")
    op.drop_column("work_package", "frontend_ref_post_id")
    op.drop_column("work_package", "ack")
    op.drop_column("work_package", "done")
    op.add_column("post_reaction", sa.Column("post_id", postgresql.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, "post_reaction", type_="foreignkey")
    op.create_foreign_key("post_reaction_post_id_fkey", "post_reaction", "post", ["post_id"], ["id"])
    op.drop_column("post_reaction", "work_package_id")
    op.drop_column("post", "children_count")
    op.drop_column("post", "depth")
    # ### end Alembic commands ###
