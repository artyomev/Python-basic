from flask import Blueprint, render_template

index_page = Blueprint(
    'index_page',
    __name__
)

@index_page.get('/', endpoint='index')
def index():
    return render_template('base.html')