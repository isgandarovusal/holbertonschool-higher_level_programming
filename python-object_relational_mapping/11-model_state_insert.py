#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
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

    # Yeni State obyekti yaradırıq
    new_state = State(name="Louisiana")

    # Obyekti session-a əlavə edirik və bazaya commit edirik
    session.add(new_state)
    session.commit()

    # Yeni yaranan ID-ni çap edirik
    print("{}".format(new_state.id))

    # Session bağlanır
    session.close()
