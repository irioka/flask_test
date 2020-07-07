from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators, SubmitField
from sqlalchemy.orm import synonym
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

class LoginForm(FlaskForm):
    email = TextField('email', validators=[validators.Required()])
    password = PasswordField('Password', validators=[validators.Required()])
    submit = SubmitField('ログイン')


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column('password', db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        if password:
            password = password.strip()
        self._password = generate_password_hash(password)
    password_descriptor = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password_descriptor)

    # フォームで送信されたパスワードの検証
    def check_password(self, password):
        password = password.strip()
        if not password:
            return False
        return check_password_hash(self.password, password)

    # 認証処理
    @classmethod
    def auth(cls, query, email, password):
        user = query(cls).filter(cls.email == email).first()
        if user is None:
            return None, False
        return user, user.check_password(password)


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
