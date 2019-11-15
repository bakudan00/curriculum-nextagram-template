import peeweedbevolve
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User
from flask_login import login_user, login_required, current_user


profile_blueprint = Blueprint('profile',
                            __name__,
                            template_folder='templates')

@profile_blueprint.route("/new", methods=['GET'])
@login_required
def new():
    return render_template('profile/new.html')
