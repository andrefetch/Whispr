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
    return render_template('home.jinja')

@app.route("/about")
def about():
    return render_template('about.jinja')

@app.route("/chat")
def chat():
    return render_template('chat.jinja')

if __name__ == "__main__":
    app.run(debug=True)
