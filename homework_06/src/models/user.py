from models.db import db

from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    name: Mapped[str] = mapped_column(unique=True)
    purchases = db.relationship('Purchase',  backref='user')

    def __repr__(self):
        return self.name
