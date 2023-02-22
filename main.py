import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from blog.repository.models.base import Base
from blog.service.simple import SimpleService


def main():
    """Entrypoint of app."""

    database_uri = os.getenv('DATABASE_URI')  # set DATABASE_URI=sqlite:///data.db
    if database_uri is None:
        database_uri = 'sqlite:///:memory:'
    engine = create_engine(database_uri)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        simple_service = SimpleService(session)
        simple_service.run()


if __name__ == '__main__':
    main()
