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

    new_state = State(name='Louisiana')
    my_session.add(new_state)
    my_session.commit()

    nstate = my_session.query(State).filter(State.name == 'Louisiana').first()
    if state:
        print(nstate.id)
    else:
        print('Not found')

    my_session.close()
