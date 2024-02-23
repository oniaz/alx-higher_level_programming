#!/usr/bin/python3


"""Listing all the states ids and names sorted asc by id"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    URI = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2],
                                                      argv[3])
    engine = create_engine(URI, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all rows from the State
    rows = session.query(State).order_by(State.id).all()
    # Print the results
    for row in rows:
        print(f"{row.id}: {row.name}")

    # Commit changes and close session
    session.commit()
    session.close()
