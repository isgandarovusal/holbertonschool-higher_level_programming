#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Session yaradılması
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adında 'a' hərfi olanları süzgəcdən keçiririk və ID-yə görə sıralayırıq
    states_with_a = session.query(State).filter(
        State.name.contains('a')).order_by(State.id).all()

    # Nəticələri çap edirik
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Session bağlanır
    session.close()
