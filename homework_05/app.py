from flask import Flask,  render_template
from views.about import about_page

app = Flask(__name__)

app.register_blueprint(about_page)


@app.get('/', endpoint='index')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)


