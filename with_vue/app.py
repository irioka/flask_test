from backend.application import create_app
from backend.api import api_bp
from flask import render_template

app = create_app()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
