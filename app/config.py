import os
from dotenv import load_dotenv


load_dotenv()

class Config:
# Aqui são chamadas as variaveis de ambiente
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///database.db")

