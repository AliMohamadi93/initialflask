from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://AliMohamadi93@mydatabase10:Vauxhallcorsa10@mydatabase10.mysql.database.azure.com/testing"
db = SQLAlchemy(app)
from os import getenv

app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
from application import routes
