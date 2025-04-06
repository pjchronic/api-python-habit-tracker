from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from app.routes import blueprints

db = SQLAlchemy()

def create_app():
    app = Flask(__name__) # inicia a aplicação
    app.config.from_object(Config) # Seta configurações do .env
    db.init_app(app) # inicializa o banco de dados
    
    # faz um loop para listar as rotas
    for bp in blueprints:
        app.register_blueprint(bp, url_prefix=f"/{bp.name}")

    return app
    