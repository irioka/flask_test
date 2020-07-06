from backend import create_app
from backend.models import TaskModel, init_db, db
from flask import render_template

app = create_app()
with app.app_context():
    init_db(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db = init_db(app)
        if not TaskModel.query.order_by(TaskModel.id.desc()).all():
            tasks = [
                TaskModel(title='foo', text='This is foo.'),
                TaskModel(title='bar', text='This is bar.'),
            ]                
            db.session.add_all(tasks)
            db.session.commit()
    app.run()
