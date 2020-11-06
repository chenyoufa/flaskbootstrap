from flask_migrate import MigrateCommand

from app import app, manager, db
from app.managerUtil.database import  database_manager
from app.views import *
from flask_script import Command, prompt_bool

# 添加其他的命令到manager里面来
manager.add_command('database', database_manager)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # app.run(port=5006,debug=True)
    manager.run()


# 1.创建迁移仓库
#  python manage.py  db init

# 2.读取类的内容, 生成版本文件, 并没有真正在数据库中添加或删除;
# python manage.py db migrate -m "添加用户性别"

# 3.在数据库中增删改, 也就是将迁移应用于数据库;
#  python manage.py  db upgrade 

# 4 返回指定的版本状态;降级数据库,不指定版本则是最老版本
#  python manage.py  db downgrade base 

# python manage.py database recreate
# python manage.py database init_data
