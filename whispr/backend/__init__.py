from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

FRONTEND_DIR = Path(__file__).resolve().parent.parent / 'frontend'

app = Flask(
    __name__,
    template_folder=str(FRONTEND_DIR / 'templates'),
    static_folder=str(FRONTEND_DIR / 'static'),
)

app.config['SECRET_KEY'] = '27f447588a5d72af7908ac6c9d0b79bb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from whispr.backend import routes