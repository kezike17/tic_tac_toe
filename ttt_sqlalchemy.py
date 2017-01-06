from sqlalchemy import Table, Column, Integer, String, Unicode, Boolean, MetaData, ForeignKey
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()

games = Table('games', metadata,
             Column('id', Integer, primary_key=True), 
             Column('board_id', String),
             Column('player1_id', String),
             Column('player2_id', String),
             Column('turn', Unicode),
             Column('is_over', Boolean)
)

boards = Table('boards', metadata,
              Column('id', Integer, primary_key=True), 
              Column('turn', Unicode)
)

players = Table('players', metadata,
               Column('id', Integer, primary_key=True), 
               Column('piece', Unicode)
)
