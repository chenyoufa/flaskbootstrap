from flask_migrate import MigrateCommand
from app import views

from app import app, manager, db
from app.managerUtil.database import  database_manager

from flask_script import Command, prompt_bool

# 添加其他的命令到manager里面来
manager.add_command('database', database_manager)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()



