#!/usr/bin/python3
"""This module prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    statename = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, dbname
    ))
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        result = (session.query(State).filter(State.name == statename).one())
        print("{}".format(result.id))
    except Exception:
        print("Not found")
