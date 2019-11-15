import peeweedbevolve
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User
from flask_login import login_user, login_required, current_user

images_blueprint =  Blueprint('images',
                            __name__,
                            template_folder='templates')

@images_blueprint.route("/new", methods=['GET'])
@login_required
def new():
    return render_template('images/new.html')

@images_blueprint.route("/<id>/update", methods=["POST"])
@login_required
def update(id):
    return "USERS"

