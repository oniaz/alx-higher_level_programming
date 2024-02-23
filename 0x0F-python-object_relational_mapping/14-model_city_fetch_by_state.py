#!/usr/bin/python3


"""Showing the city name and id and the state name"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    URI = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2],
                                                      argv[3])
    engine = create_engine(URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State.name, City.id, City.name).join(
                    City, State.id == City.state_id).order_by(City.id).all()

    for row in rows:
        print(f"{row[0]}: ({row[1]}) {row[2]}")

    session.close()
