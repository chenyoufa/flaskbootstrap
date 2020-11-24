from flask_script import Manager, prompt_bool, Command
from app import db
from app.models import User, Role,UserBelong,Menus


database_manager  = Manager(usage="数据库的操作详情")
# 1. 方法一： 类的继承
class AddUser(Command):
    """添加用户"""
    def run(self):
        u = User(username="fentiao90009", password="fentiao", email="fentiao@qq.com")
        db.session.add(u)
        db.session.commit()
        return "正在添加用户%s........" % (u.username)
# 添加类到命令中， 让manger进行管理
database_manager.add_command('adduser', AddUser)


# 2. 通过装饰器@database_manager.command
@database_manager.command
def deleteUser():
    """删除用户"""
    u = User.query.filter_by(username='fentiao90009').first()
    if u:
        db.session.delete(u)
        db.session.commit()
        return "删除用户%s成功....." % (u.username)
    else:
        return "删除用户失败:"


# 3). option装饰器， 可以指定参数
@database_manager.option('-u', '--username', help="指定用户名")
@database_manager.option('-p', '--password', help="指定密码")
def add_user(username, password):
    """添加用户， 指定用户名和密码"""
    if username and password:
        u = User(username=username, password=password)
        db.session.add(u)
        db.session.commit()
        return  "添加用户%s成功" %(u.username)
    else:
        return  "请指定用户名和密码"




@database_manager.command
def dropdb():
    """删除数据库"""
    if prompt_bool("是否删除数据库"):
        db.drop_all()

#python manage.py database createdb
@database_manager.command
def createdb():
    """创建数据库"""
    if prompt_bool("是否创建数据库"):
        db.create_all()


@database_manager.command
def recreate():
    """重建数据库"""
    if prompt_bool("是否重数据库"):
        dropdb()
        createdb()


@database_manager.command
def init_data():
    """初始化数据库"""
    
    
    user = User(UserName="fage", PassWord="123456", Email="879756530@qq.com" ,
    Status=1,CreateUserid=1,ModifyUserid=1)
    db.session.add(user)

    belong = UserBelong(Belongid=1,BelongType=1,Status=1,CreateUserid=1,ModifyUserid=1)
    db.session.add(belong)


    role = Role(Name="超级管理员",Status=1,CreateUserid=1,ModifyUserid=1)
    db.session.add(role)
    role = Role(Name="普通管理员",Status=1,CreateUserid=1,ModifyUserid=1)
    db.session.add(role)
    for user in range(100):
        u = User(UserName="westos%s" %(user), PassWord="hello", 
        Email="westos%s@qq.com"  %(user),Status=1,CreateUserid=1,ModifyUserid=1)
        db.session.add(u)
    menu = Menus(ParentId=0,MenuName='系统工具',MenuUrl="",MenuType="1",MenuTarget="",
    Status=1,CreateUserid=1,ModifyUserid=1,MenuIcon="")
    db.session.add(menu)
    menu = Menus(ParentId=1,MenuName='通用字典',
    MenuUrl="SystemManage/DataDict/DataDictIndex",MenuType="2",MenuTarget="",
    Status=1,CreateUserid=1,ModifyUserid=1,Authorize="system:datadict:view",MenuIcon="")
    db.session.add(menu)
    db.session.commit()
    print("初始化完成")