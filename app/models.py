### 用户和角色是什么关系?
#    - 一对一
#    - 一对多: 角色是一， 用户是多， 外键写在多的一端
#   - 多对多
from datetime import datetime
from app import db,AbstractConcreteBase
from sqlalchemy.orm import relationship

# 配合多个对象使用的函数
def to_json(lists):
        # print(lists)
        v = [ ven.dobule_to_dict() for ven in lists ]
        return v

class Entry(AbstractConcreteBase, db.Model):
    # def to_dict(self):
    #     model_dict = dict(self.__dict__)
    #     del model_dict['_sa_instance_state']
    #     return model_dict
    # def single_to_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    Id = db.Column(db.Integer, primary_key=True)
    CreateUserid=db.Column(db.SmallInteger,nullable=False)
    CreateTime = db.Column(db.DateTime, default=datetime.now())
    ModifyTime = db.Column(db.DateTime, default=datetime.now())
    ModifyUserid=db.Column(db.SmallInteger,nullable=False)
    Status = db.Column(db.SmallInteger,default=1)
    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result
    def test(self):
        return self



class Role(Entry):
    __tablename__ = "SysRoles"
    # id号递增autoincrement=True

    Name = db.Column(db.String(20))
    Sort=db.Column(db.SmallInteger,nullable=True,default=0)
    Remark= db.Column(db.String(20))

    # 反向引用, Role表中有属性users， User类中有role这个属性;
    # Users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role %s>" % (self.Name)

class User(Entry):
    __tablename__ = "SysUsers"

    UserName = db.Column(db.String(30), unique=True, index=True, nullable=False)  # unique=True用户名不能重复,index 自增 nullable 是否可空
    PassWord = db.Column(db.String(150), nullable=False)
    RealName = db.Column(db.String(20), unique=False)
    Email = db.Column(db.String(50), unique=True)
    Mobile= db.Column(db.String(11), unique=False)
     # 1-男 2-女
    Gender = db.Column(db.SmallInteger,default=2)
    Salt= db.Column(db.String(4), unique=False)
    IsOnLine= db.Column(db.SmallInteger,default=0)
    LastTime= db.Column(db.DateTime, default=datetime.now())
    LastIp= db.Column(db.String(20), unique=False)
    Portrait= db.Column(db.String(200), unique=False)
    # 设置默认值， 位当前用户的创建时间;
    Belongs = db.relationship('UserBelong', backref='Belong')
    #### 重要的： 用户角色id不能随便设置， 需要从Role中查询, （外键关联）
    # RoleId = db.Column(db.Integer, db.ForeignKey('sysRole.id'))
# 单个对象方法1
    
    
    # 定义了 __repr()__ 方法,返回一个具有可读性的字符串表示模型,可在调试和测试时使用。
    def __repr__(self):
        return "<User %s>" % (self.UserName)

class UserBelong(Entry):
    __tablename__ = "SysUserBelongs"
    # UserId=db.Column(db.SmallInteger,nullable=False)
    Belongid=db.Column(db.SmallInteger,nullable=False)
    BelongType=db.Column(db.SmallInteger,nullable=False)
    UserId = db.Column(db.Integer, db.ForeignKey('SysUsers.Id'))
    Remark= db.Column(db.String(20))
    # 反向引用, Role表中有属性users， User类中有role这个属性;
    # Users = db.relationship('User', backref='Roles')
    def __repr__(self):
        return "<UserBelong %s>" % (self.UserId)

class Menus(Entry):
    __tablename__ = "SysMenus"
    ParentId=db.Column(db.SmallInteger,nullable=False)
    MenuName = db.Column(db.String(50), nullable=False)
    MenuIcon = db.Column(db.String(50))
    MenuUrl = db.Column(db.String(100))
    MenuTarget = db.Column(db.String(50),)
    MenuSort=db.Column(db.SmallInteger)
    MenuType=db.Column(db.SmallInteger,nullable=False) # 1目录 2页面 3按钮
    Authorize = db.Column(db.String(50))
    Remark= db.Column(db.String(20))
    # 设置默认值， 位当前用户的创建时间;
    # 定义了 __repr()__ 方法,返回一个具有可读性的字符串表示模型,可在调试和测试时使用。
    def __repr__(self):
        return "<Menus %s>" % (self.MenuName)

class SysLog(Entry):
    __tablename__ = "SysLog"
    # UseName = db.Column(db.String(30),comment="登录名称")
    UserId  = db.Column(db.Integer,db.ForeignKey('SysUsers.Id'))
    IpAddress = db.Column(db.String(30),comment="ip地址")
    IpHome = db.Column(db.String(60),comment="ip归属地")
    AgentBrowser = db.Column(db.String(60),comment="浏览器")
    OperatingSystem = db.Column(db.String(60),comment="操作系统")
    LogCategory = db.Column(db.Integer,primary_key=False,comment="日志列表")#1登录日志，2操作日志
    OperatingInfo = OperatingSystem = db.Column(db.String(60),comment="操作信息")
    # DepartmentName = db.Column(db.String(30),comment="部门名称")
    OperationMethod = db.Column(db.String(30),comment="操作方法")
    TimeConsue = db.Column(db.Integer,primary_key=False,comment="耗时")
    Parameter = db.Column(db.String(60),comment="请求参数")

class Department(Entry):
    __tablename__ = "SysDepartment"
    DepartName = db.Column(db.String(50))
    ParentId =  db.Column(db.Integer)
    DepartSort = db.Column(db.Integer)
    Email = db.Column(db.String(50), unique=True)
    Fax = db.Column(db.String(50), unique=True)
    Mobile = db.Column(db.String(11), unique=False)
    User_id = db.Column(db.Integer,db.ForeignKey('SysUsers.Id'))
    Remarks =  db.Column(db.String(200), unique=True)
    # to_user =  relationship("User",backref = "Dep2User")

    def __repr__(self):
        return "<Department %s>" % (self.UserName)

