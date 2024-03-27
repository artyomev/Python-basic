from .base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Post(Base):

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)
    user = relationship("User", back_populates="posts")

    def __str__(self):
        return (f"Post(id = {self.id}, "
                f"title={self.title}, "
                f"user_id = {self.user_id}")