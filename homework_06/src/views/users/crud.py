"""
Create
Read
Update
Delete
"""
from sqlalchemy import select
from models.db import db
from models.user import User


def create_user(name: str) -> User:
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user


def get_users() -> list[User]:

    return list(db.session.scalars(select(User)).all())


def get_user(user_id: int) -> User | None:

    return User.query.get(user_id)