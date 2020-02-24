from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://ali:password@127.0.0.1/flaskapp"
db = SQLAlchemy(app)

from application import routes
