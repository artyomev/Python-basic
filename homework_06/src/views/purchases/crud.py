"""
Create
Read
Update
Delete
"""
from sqlalchemy import select
from models.db import db
from models.purchase import Purchase
from models.user import User


def create_purchase(product_name: str,
                    cost: float,
                    user: User) -> Purchase:
    purchase = Purchase(product_name=product_name, cost=cost, user=user)
    db.session.add(purchase)
    db.session.commit()
    return purchase


def get_purchases() -> list[Purchase]:

    return list(db.session.scalars(select(Purchase)).all())


def get_purchase(purchase_id: int) -> Purchase | None:

    return Purchase.query.get(purchase_id)