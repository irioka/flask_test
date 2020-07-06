from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            text=self.text
        )

    def __repr__(self):
        return '<Task id={id} title={title!r}>'.format(id=self.id, title=self.title)


def init_db(app):
    db.init_app(app)
    db.create_all()
    return db


# def insert(name, note):
#     model = SpamModel(name=name, note=note)
#     db.session.add(model)
#     db.session.commit()
