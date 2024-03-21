#!/usr/bin/python3

"""
Adds a new state and prints its id.
Must be fun
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/'
                           '{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    my_session = Session()

    new_name = 'New Mexico'
    old_state = my_session.query(State).filter(State.id == 2).first()
    old_state.name = new_name

    my_session.commit()

    my_session.close()
