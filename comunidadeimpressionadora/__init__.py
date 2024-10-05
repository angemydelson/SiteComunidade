from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

lista_usuarios = ['Lira', 'João', 'Alon', 'Alessandra', 'Amanda']

app.config['SECRET_KEY'] = '9a2b9c1232582c7952c3dd35b018441b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from comunidadeimpressionadora import routes