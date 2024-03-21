#!/usr/bin/python3

"""
Creates the State 'California' with the City 'San Francisco'
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    usr_nm = sys.argv[1]
    passwd = sys.argv[2]
    the_db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr_nm, passwd, the_db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    my_session = Session()

    cali = State(name="California")
    san_fra = City(name="San Francisco")
    cali.cities.append(san_fra)

    my_session.add(cali)

    my_session.commit()

    my_session.close()
