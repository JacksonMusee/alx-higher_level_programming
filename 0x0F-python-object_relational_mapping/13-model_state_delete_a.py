#!/usr/bin/python3

"""
Deletes all states whose name contai 'a'
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

    a_states = my_session.query(State).filter(State.name.like('%a%')).all()
    for state in a_states:
        my_session.delete(state)

    my_session.commit()

    my_session.close()
