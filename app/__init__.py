from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import AbstractConcreteBase
import pymysql
from flask_script import  Manager
from flask_migrate import  Migrate
from flask_wtf.csrf  import CSRFProtect

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config.from_pyfile('../config.py')
csrf = CSRFProtect(app)                   # 加入这行代码就可以了
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)