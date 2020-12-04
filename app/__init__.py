from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import AbstractConcreteBase
import pymysql
from flask_script import  Manager
from flask_migrate import  Migrate
from flask_wtf.csrf  import CSRFProtect
from utils.Log import AppLog
from flask import current_app

pymysql.install_as_MySQLdb()
app = Flask(__name__)
ctx = app.app_context()
ctx.push()
app.config.from_pyfile('../config.py')
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
# 日志初始化
AppLog.init_log(current_app.config.get("LOG_PATH"))