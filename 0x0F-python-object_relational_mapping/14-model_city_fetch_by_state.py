#!/usr/bin/python3
""" Module for task 14 """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
            .filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
