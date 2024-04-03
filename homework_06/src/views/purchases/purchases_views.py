from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for, flash,

)

from forms.forms import PurchaseForm
from models.purchase import Purchase
from models.db import  db
from views.purchases import crud
from views.users.crud import get_user

purchases_app = Blueprint(
    "purchases_app",
    __name__,
    url_prefix="/purchases",
)


@purchases_app.get(
    "/",
    endpoint="list",
)
def get_purchases():
    return render_template(
        "purchases/list.html",
        purchases=crud.get_purchases(),
    )


@purchases_app.route(
    "/add/",
    endpoint="add",
    methods=["GET", "POST"],
)
def create_purchase():
    form = PurchaseForm()
    if request.method == "GET":
        return render_template("purchases/add.html", form=form)
    if form.validate_on_submit():

        product_name = form.product_name.data
        product_name = product_name.strip()
        cost = form.cost.data
        cost = float('%.2f' % cost)
        user = get_user(form.user.data.id)
        purchase = crud.create_purchase(
            product_name=product_name,
            cost = cost,
            user=user
        )

        flash(f"Created purchase"
              f" {product_name!r}!", category="success")

        url = url_for(
            "purchases_app.details",
            purchase_id=purchase.id,
        )
        return redirect(url)


@purchases_app.get(
    "/<int:purchase_id>/",
    endpoint="details",

)
def get_purchase_details(purchase_id: int):
    purchase: Purchase = Purchase.query.get_or_404(
        purchase_id,
        description=f"Purchase #{purchase_id} not found!",
    )
    return render_template(
        "purchases/details.html",
        purchase=purchase
    )


@purchases_app.route(
    "/<int:purchase_id>/confirm-delete/",
    endpoint="delete",
    methods=["GET", "POST"],
)
def delete_purchase(purchase_id: int):
    purchase: Purchase = Purchase.query.get_or_404(
        purchase_id,
        description=f"Purchase#{purchase_id} not found!",
    )
    if request.method == "GET":
        return render_template(
            "purchases/delete.html",
            purchase=purchase
        )

    purchase_name = purchase.product_name
    db.session.delete(purchase)
    db.session.commit()

    flash(f"Deleted {purchase_name!r} successfully!", category="warning")
    url = url_for("purchases_app.list")
    return redirect(url)