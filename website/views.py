from flask import Blueprint, render_template
from flask_login import login_required, current_user, logout_user
views = Blueprint('views', __name__, template_folder='templates')


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/logout_strona')
def logout_strona():
    logout_user()
    return render_template("logout_strona.html", user=current_user)

