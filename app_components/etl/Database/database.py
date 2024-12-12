import os
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base

# Load environment variables from a .env file
load_dotenv()


DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.drop_all(engine)


def get_db():
    """
    Yields a SQLAlchemy database session and ensures proper cleanup.

    Yields:
        Session: A database session instance.

    Usage:
        Use as a dependency or utility for database operations.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()