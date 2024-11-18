from flask import Flask, render_template, redirect, url_for, flash , request
from utils import db
import os
from flask_migrate import Migrate
from models.Usuario import Usuario
from controllers.Usuario import bp_usuarios

app = Flask(__name__)
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_host = os.getenv('DB_HOST')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_mydb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
