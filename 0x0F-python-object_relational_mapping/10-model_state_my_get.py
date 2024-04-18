#!/usr/bin/python3
"""List all states"""
import stat
from sys import argv

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_conn_str = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(db_conn_str, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == argv[4]).\
        order_by(State.id).all()
    if state:
        print(state[0].id)
    else:
        print("Not found")

    session.close()
