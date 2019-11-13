import peeweedbevolve
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User
from flask_login import login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash


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
    return "USERS"

    # username = request.form.get('username')
    # email = request.form.get('email')
    # password = request.form.get('password')
    # chk_password = check_password_hash(current_user.password, password)
    # user = User.get_by_id(id)
    # if current_user.id == user.id:
    #     if chk_password:
    #         if current_user.username != username:
    #             updated_user = user.update(username=username).where(user.id == current_user.id)
    #             updated_user.execute()
    #         if current_user.email != email:
    #             updated_user = user.update(email=email).where(user.id == current_user.id)
    #             updated_user.execute()
    #         if current_user.password != password:
    #             updated_user = user.update(password=generate_password_hash(password)).where(user.id == current_user.id)
    #         flash('update succesfully!')
    #         return render_template('users/edit.html', id=id)
    #     else:
    #         flash('kindly ensure that initial password matches')
    #         return render_template('users/edit.html', id=id)
    # else:
    #     flash('wrong id to update')
    #     return render_template('users/edit.html', id=id)

    # upd_user = User(username=username, email=email, password=password)
    # if current_user.id == user.id:
    #     if upd_user.save():
    #         flash(f"{user.username} profile page is updated!") 
    #         return redirect(url_for('users.edit', id=id)) 
    #     else:
    #         flash(f"update profile page failed!") 
    #         return render_template('users/edit.html', id=id)
    # else:
    #     flash('invalid credentials')
    #     return render_template('users/edit.html', id=id)
