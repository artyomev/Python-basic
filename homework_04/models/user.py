from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship



class User(Base):

    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    posts = relationship("Post", back_populates="user")
