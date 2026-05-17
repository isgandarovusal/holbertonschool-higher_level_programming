#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Engine yaradılır və sətir uzunluğu limitinə diqqət edilir
    conn_str = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(conn_str.format(sys.argv[1], sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)

    # Session yaradılması
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adına görə süzgəcləyirik
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Nəticəni yoxlayırıq
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Session bağlanır
    session.close()
