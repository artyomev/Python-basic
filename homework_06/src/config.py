import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    "postgresql+psycopg://postgres:admin@localhost:5432/postgres",
)
SQLALCHEMY_ECHO = False