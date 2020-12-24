from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import AbstractConcreteBase
import pymysql
from flask_script import  Manager
from flask_migrate import  Migrate
from flask_wtf.csrf  import CSRFProtect
from utils.Log import Logger

pymysql.install_as_MySQLdb()
curre_app = Flask(__name__)
ctx = curre_app.app_context()
ctx.push()
curre_app.config.from_pyfile('../config.py')
csrf = CSRFProtect(curre_app)
db = SQLAlchemy(curre_app)
manager = Manager(curre_app)
migrate = Migrate(curre_app, db)
curre_app.secret_key = 'please-generate-a-random-secret_key'
# # 日志初始化
# Logger.init_app(curre_app,db)