from flask import Flask, render_template
import os

app = Flask(
    __name__,
    template_folder=os.path.join('..', 'frontend', 'templates'),
    static_folder=os.path.join('..', 'frontend', 'static'),
)

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


@app.route("/login")
def login():
    return render_template('auth/login.jinja', title="Login")

@app.route('/signup')
def signup():
    return render_template('auth/signUp.jinja', title="Sign Up")

if __name__ == "__main__":
    app.run(debug=True)