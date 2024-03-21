#!/usr/bin/python3

"""
Lists all City objects from the database hbtn_0e_101_usa
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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(usr_nm, passwd, the_db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    cities_with_state = my_session.query(City).order_by(City.id)

    for city in cities_with_state:
        print(f'{city.id}: {city.name} -> {city.state.name}')

    my_session.close()
