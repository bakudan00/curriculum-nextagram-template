import peeweedbevolve
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User
from flask_login import login_user, login_required, current_user


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user_create = User(username=username, email=email, password=password)

    if user_create.save():
        flash('added successfully!')
        return redirect(url_for('users.new'))
    else:
        for errors in user_create.errors:
            flash(errors)
            return render_template('users/new.html', username=username, email=email, password=password)
    
@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass

@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"

@users_blueprint.route('/<id>/edit', methods=['GET'])
@login_required
def edit(id):
    user = User.get_by_id(id)
    if current_user.id == user.id:
        return render_template('users/edit.html', id=id)
    else:
        flash(f"invalid access to {user.username} page")
        return render_template('users/edit.html', id=id)

@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
        pass
