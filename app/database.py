from flask_sqlalchemy import SQLAlchemy
from app.config import Config


db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        db.create_all()
