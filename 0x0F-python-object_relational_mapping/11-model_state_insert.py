#!/usr/bin/python3


"""Adding a new record to the 'States' table"""


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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
