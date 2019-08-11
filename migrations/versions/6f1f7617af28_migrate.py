"""'migrate'

Revision ID: 6f1f7617af28
Revises: 
Create Date: 2019-08-11 23:22:55.818478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f1f7617af28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_bora')
    op.drop_table('todo_song')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_song',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('todo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('regdate', mysql.DATETIME(), nullable=False),
    sa.Column('complete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    op.create_table('todo_bora',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('todo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('regdate', mysql.DATETIME(), nullable=False),
    sa.Column('complete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    # ### end Alembic commands ###