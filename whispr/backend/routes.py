from flask import render_template, url_for, flash, redirect, request
from whispr.backend import app, db, bcrypt
from whispr.backend.forms import RegistrationForm, LoginForm
from whispr.backend.models import User, Chatroom, Message
from flask_login import login_user, current_user, logout_user, login_required


# Flask renders routes by using decorators ex: @app.route, then the "/" goes from root to another page, you can use these routes to different jinja templates (or whatever HTML5 type you want to use)
@app.route("/")
@app.route('/home')
def home():
    return render_template('home.jinja', title="Whispr")

@app.route("/chat")
@login_required
def chat():
    return render_template('chat.jinja', title="Chat")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f' User: "{user.username}" → Login successful.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('chat'))
        else:
            flash('Login Failed. Please check email and password.', 'danger')
    return render_template('auth/login.jinja', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST']) # Accepts both Get & Post methods.
def register():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account has been created, you can now login.', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.jinja', title="Sign Up", form=form)

@app.route("/logout")
@login_required
def logout():
    try:
        username = current_user.username
        logout_user()
        flash(f'User: "{username}" has logged out successfully.', 'success')
        return redirect(url_for('home'))
    except:
        flash(f"Error logging out, check console", 'danger')
        raise Exception("Error logging out.")

@app.route("/account")
@login_required
def account():
    return render_template('account.jinja', title='Account')