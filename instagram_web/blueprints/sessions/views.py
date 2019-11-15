import peeweedbevolve
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from instagram_web.util.google_oauth import oauth
from models.user import User
from flask_login import login_user, logout_user, login_required
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
            login_user(user)
            flash('Login Success!!')
            return redirect(url_for('home'))
        else:
            flash('wrong password!')
            return render_template('sessions/new.html')
    else:
        flash('user not found')
        return render_template('sessions/new.html')

@sessions_blueprint.route('/login/google', methods=["GET"])
def login_google():
    redirect_uri = url_for('sessions.authorize_google', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@sessions_blueprint.route("/authorize/google", methods=["GET"])
def authorize_google():
    token = oauth.google.authorize_access_token()
    if not token:
        flash('unable to retrieved the token')
        return redirect(url_for('home'))
        
    email = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()['email']
    user = User.get_or_none(email=email)
    if not user:
        flash('email not register yet')
        return redirect(url_for('home'))
    else:
        login_user(user)
        return redirect(url_for('home'))

    
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
@login_required
def destroy():
    logout_user()
    flash('successfully logout')
    return redirect(url_for('home'))
    
