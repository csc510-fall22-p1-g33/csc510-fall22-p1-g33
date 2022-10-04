from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from ..extensions import db
from ..models.all import User
# from ..models.user import User
# from ..models.team import Team
# from ..models.project import Project

import functools
from werkzeug.security import check_password_hash, generate_password_hash

registerer = Blueprint('auth', __name__, url_prefix='/auth')
@registerer.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                user = User((username, generate_password_hash(password)))
                db.session.add(user)
                db.session.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return {"error":"400","message":"Bad request. Invalid details provided"}
    return {"success":"200"}


@registerer.route('/login', methods =['GET', 'POST'])
def login():   # to handle login operations
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if password:
            password = generate_password_hash(password)
        user = db.session.query(username=username, password=password).first()
        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            msg = 'Logged in successfully !'
            return {"success":"200","message":msg}
        else:
            msg = 'Incorrect username / password !'
    else:
        return {"error":"405","message":"Unknown method used"}
    return {"error":"404","message":msg}
  
@registerer.route('/logout')
def logout():    # to handle logout operations
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return {"success":"200","message":"Successfully logged out"}