from flask_wtf import FlaskForm
from wtforms import (StringField)
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.fields.numeric import FloatField
from wtforms.validators import InputRequired, Length, NumberRange


from views.users.crud import get_users


class PurchaseForm(FlaskForm):
    product_name = StringField('Product Name', validators=[InputRequired(),
                                                           Length(min=1, max=300)])
    cost = FloatField('Cost', validators=[NumberRange(0)])
    user = QuerySelectField(query_factory=get_users, get_label="name", validators=[InputRequired()])