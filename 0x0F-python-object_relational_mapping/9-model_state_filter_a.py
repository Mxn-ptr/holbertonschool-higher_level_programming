#!/usr/bin/python3
""" Module for task 9 """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id):
    if "a" in state.name:
        print("{}: {}".format(state.id, state.name))

session.close()
