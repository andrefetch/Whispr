from flask import render_template, url_for, flash, redirect 
from whispr.backend import app
from whispr.backend.forms import RegistrationForm, LoginForm
from whispr.backend.models import User, Chatroom, Message


# Flask renders routes by using decorators ex: @app.route, then the "/" goes from root to another page, you can use these routes to different jinja templates (or whatever HTML5 type you want to use)
@app.route("/")
@app.route('/home')
def home():
    return render_template('home.jinja', title="Whispr")

@app.route("/chat")
def chat():
    return render_template('chat.jinja', title="Chat")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@thing.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('chat'))
        else:
            flash('Login Failed. Please check username and password.', 'danger')
    return render_template('auth/login.jinja', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST']) # Accepts both Get & Post methods.
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('chat'))
    return render_template('auth/register.jinja', title="Sign Up", form=form)