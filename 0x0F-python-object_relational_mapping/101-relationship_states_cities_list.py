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
    """
    cities_with_state = my_session.query(City).order_by(City.id)
    
    state_list = []
    for city in cities_with_state:
        state = (city.state.id, city.state.name)
        if state not in state_list:
            state_list.append(state)

    for item in state_list:
        print(f'{item[0]}: {item[1]}')

        for city in cities_with_state:
            if city.state.id == item[0]:
                print(f'    {city.id}: {city.name}')
    """

    states_with_cities = my_session.query(State).order_by(State.id)

    for state in states_with_cities:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'    {city.id}: {city.name}')

    my_session.close()
