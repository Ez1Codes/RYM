from main import app
from flask import render_template, redirect, url_for, flash, request
from main.models import User, db
from main.forms import RegisterForm, LoginForm, ActivitiesForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    
    users = User.query.all()
    if request =='GET':
        activity = ActivitiesForm()
        current_activity = request.form.activity('cur_activity')

    return render_template('home.html', users=users)

"""@app.route('/main', methods=['GET', 'POST'])
@login_required
def main_page():
    if request.method == 'GET':
        users = User.query.all()
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('main.html', items=items, users=users,purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)
"""

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                                email=form.email_address.data,
                                password=form.password1.data,
                                about=form.about.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash('Account ceated successfully! ', category='success')
        return redirect(url_for('home_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash('Success', category='successs')
            return redirect(url_for('home_page')) 
        else:
            flash('Username and password are not match, please try again!', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have successfully logged out", category='info')
    return redirect(url_for("home_page"))

@app.route('/blog')
def blog_page():
    return render_template('blogpage.html')