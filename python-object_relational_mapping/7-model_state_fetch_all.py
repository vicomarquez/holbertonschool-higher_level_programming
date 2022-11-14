#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import MySQLdb

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    res = session.query(State).all()

    for state in res.order_by(State.id):
        print('{}: {}'.format(state.id, state.name))

    session.close()
