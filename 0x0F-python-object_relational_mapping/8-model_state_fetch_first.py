#!/usr/bin/python3


"""Listing the first state's id and name from the 'States' table"""


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
    row = session.query(State).order_by(State.id).first()
    # Print the results
    if row:
        print(f"{row.id}: {row.name}")

    # Commit changes and close session
    session.commit()
    session.close()
