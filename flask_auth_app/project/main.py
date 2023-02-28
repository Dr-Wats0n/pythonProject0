# main.py

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('calculator.html')
    else:
        return render_template('result.html', premium_value=request.form['premium_value'], plan_a1 = request.form['plan_a1'], fact_a1 = request.form['fact_a1'])



@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)