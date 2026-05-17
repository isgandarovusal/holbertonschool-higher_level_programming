#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
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

    # id = 2 olan state obyektini tapırıq
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Əgər obyekt tapılarsa, adını dəyişirik və commit edirik
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Session bağlanır
    session.close()
