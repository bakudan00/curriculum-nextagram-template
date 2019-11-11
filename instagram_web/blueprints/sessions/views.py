import peeweedbevolve
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user import User
from flask_login import login_user
from werkzeug.security import check_password_hash


sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')


@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('sessions/new.html')


@sessions_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.get_or_none(username=username)

    if user:
        chk_password = check_password_hash(user.password, password)
        if chk_password:
            session['user_id'] = user.id
            # login_user(user)
            flash('Login Success!!')
            return redirect(url_for('home'))
        else:
            flash('wrong password!')
            return render_template('sessions/new.html')
    else:
        flash('user not found')
        return render_template('sessions/new.html')
    
@sessions_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass

@sessions_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"

@sessions_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass

@sessions_blueprint.route('/delete')
def destroy():
    session.pop('user_id', None)
    flash('log out success')
    return redirect(url_for('home'))
    
