from backend.models import UserModel, LoginForm, db
from flask import Blueprint, redirect, request, render_template, url_for
from flask_login import login_user, logout_user


view = Blueprint('app', __name__,
                 template_folder='templates',
                 static_folder='templates/static')


@view.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user, authenticated = UserModel.auth(
            db.session.query, form.email.data, form.password.data)
        if authenticated:
            login_user(user, remember=True)
            print('Login successfully.')
            return redirect('/tasks')
        else:
            print('Login failed.')
    return render_template('login.html', form=form, action=url_for('app.login'))


@view.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect('/login')
