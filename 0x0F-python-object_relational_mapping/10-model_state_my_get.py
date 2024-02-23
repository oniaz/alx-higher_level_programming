#!/usr/bin/python3


"""Listing all the id of the state passed as an argument"""


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
    result = session.query(State.id).filter(State.name == argv[4]).first()
    # Print the results
    if result:
        print(result.id)
    else:
        print("Not found")

    # Commit changes and close session
    session.commit()
    session.close()
