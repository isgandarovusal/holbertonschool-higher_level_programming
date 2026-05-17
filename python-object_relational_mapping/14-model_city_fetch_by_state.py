#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    u, p, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(u, p, db), pool_pre_ping=True)

    # Session yaradılması
    Session = sessionmaker(bind=engine)
    session = Session()

    # Cities və States cədvəllərini JOIN edirik
    # Nəticələri cities.id-yə görə sıralayırıq
    results = session.query(State, City).filter(State.id == City.state_id).\
        order_by(City.id).all()

    # Nəticələri formatlı şəkildə çap edirik
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Session bağlanır
    session.close()
