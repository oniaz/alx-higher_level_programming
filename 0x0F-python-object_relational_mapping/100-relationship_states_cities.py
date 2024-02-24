#!/usr/bin/python3


"""Createing the state 'California' with the City 'San Francisco'."""


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

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_city)

    session.commit()
    session.close()
