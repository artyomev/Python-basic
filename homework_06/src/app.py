from flask import Flask

from views.purchases.purchases_views import purchases_app

from views.users.users_views import users_app
from views.index import index_page
from models.db import db
import config

app = Flask(__name__)

app.config.update(
    SECRET_KEY="verylongandsecretkey",
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
)


app.register_blueprint(users_app)
app.register_blueprint(index_page)
app.register_blueprint(purchases_app)

db.init_app(app)

with app.app_context():

    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


