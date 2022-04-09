#!/usr/bin/python3
""" Module for task 10 """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            flag = True
            break
        else:
            flag = False
    if flag is False:
        print("Not found")

    session.close()
