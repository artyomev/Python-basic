from models.db import db

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Purchase(db.Model):
    __table_args__ = {'extend_existing': True}
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    product_name: Mapped[str] = mapped_column(String(250), nullable=False)
    cost: Mapped[float] = mapped_column(nullable=False)



