#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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

    # Adında 'a' olan bütün ştatları tapırıq
    states_to_delete = session.query(State).filter(State.name.contains('a'))

    # Tapılan bütün qeydləri silirik
    # synchronize_session=False performansı artırır və birbaşa silir
    for state in states_to_delete:
        session.delete(state)

    # Dəyişiklikləri təsdiqləyirik
    session.commit()

    # Session bağlanır
    session.close()
