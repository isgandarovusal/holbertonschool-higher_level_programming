#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
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

    # Birinci state obyektini id-yə görə sıralayıb götürürük
    first_state = session.query(State).order_by(State.id).first()

    # Əgər nəticə varsa çap et, yoxdursa "Nothing" çap et
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Session bağlanır
    session.close()
