from flask import Flask, render_template, url_for, flash, redirect 
from forms import RegistrationForm, LoginForm
import os

app = Flask(
    __name__,
    template_folder=os.path.join('..', 'frontend', 'templates'),
    static_folder=os.path.join('..', 'frontend', 'static'),
)

app.config['SECRET_KEY'] = '27f447588a5d72af7908ac6c9d0b79bb'

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.jinja', title="Home")

@app.route("/about")
def about():
    return render_template('about.jinja', title="About")

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

if __name__ == "__main__": # Main entry point :)
    app.run(debug=True)