from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_script import  Manager
from flask_migrate import  Migrate

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)