#!/usr/bin/python3

"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    usr_nm = sys.argv[1]
    passwd = sys.argv[2]
    the_db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(usr_nm, passwd, the_db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    my_session = Session()

    all_cities = my_session.query(City)\
                           .options(joinedload(City.state))\
                           .order_by(City.id)
    for city in all_cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    my_session.close()
