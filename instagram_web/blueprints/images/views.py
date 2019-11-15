import peeweedbevolve
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User
from models.image import Image
from flask_login import login_user, login_required, current_user
from ...util.helpers import *
from werkzeug.utils import secure_filename
from app import app

images_blueprint =  Blueprint('images',
                            __name__,
                            template_folder='templates')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.'in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@images_blueprint.route("/new", methods=['GET'])
@login_required
def new():
    return render_template('images/new.html')

@images_blueprint.route("/<id>/update", methods=["POST"])
@login_required
def upload_user(id):
    if 'user_profile_image' not in request.files:
        flash('filedid not select yet')
        return(redirect(url_for('users.edit', id=id)))
    
    file = request.files['user_profile_image']

    if file.filename == "":
        flash('Pleas select a file')
        return redirect(url_for('images.new', id=id))
    else:
        if file and allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            output = upload_file_to_s3(file, app.config["S3_BUCKET"])
            profile_image = Image(imageURL=file.filename, user_id=id)
            if profile_image.save():
                flash(f'upload {str(output)} completed!')
                return redirect(url_for('images.new', id=id))
            else:
                flash('the file is corrupted please try again')
                return render_template('images/new.html', id=id)
        else:
            flash('the file is not jpeg, png, gif. please upload with correct format')
            return redirect(url_for('images.new', id=id))