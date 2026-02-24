import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave-padrao-segura')
    FLASK_APP = os.getenv('FLASK_APP', 'run.py')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    # Adicione aqui outras configurações como DATABASE_URL, etc
