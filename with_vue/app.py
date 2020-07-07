from backend import app
from backend.models import TaskModel, UserModel, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not TaskModel.query.order_by(TaskModel.id.desc()).all():
            tasks = [
                TaskModel(title='foo', text='This is foo.'),
                TaskModel(title='bar', text='This is bar.'),
            ]
            db.session.add_all(tasks)
            db.session.commit()
        if not UserModel.query.order_by(UserModel.id.desc()).all():
            user = UserModel(name='test_user', email='test@example.com')
            user._set_password('password')
            db.session.add(user)
            db.session.commit()
    app.run()
