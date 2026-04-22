"""

Hello Developers,
everything in here should be fully documented so you can understand what is going on in my slop code
if you need any help please PM me @vstpirater on discord.

"""

import uuid
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect 
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import os

app = Flask(
    __name__,
    template_folder=os.path.join('..', 'frontend', 'templates'),
    static_folder=os.path.join('..', 'frontend', 'static'),
)

app.config['SECRET_KEY'] = '27f447588a5d72af7908ac6c9d0b79bb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    chatrooms = db.relationship('Chatroom', backref='owner', lazy=True,
                                cascade='all, delete-orphan')
    messages = db.relationship('Message', backref='author', lazy=True,
                               cascade='all, delete-orphan')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Chatroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(32), unique=True, nullable=False,
                     default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.relationship('Message', backref='chatroom', lazy=True,
                               cascade='all, delete-orphan')
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatroom.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

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