### 用户和角色是什么关系?
#    - 一对一
#    - 一对多: 角色是一， 用户是多， 外键写在多的一端
#   - 多对多
from datetime import datetime
from app import db

class Role(db.Model):
    __tablename__ = "SysRoles"
    # id号递增autoincrement=True
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(20))
    Sort=db.Column(db.SmallInteger,nullable=False)
    Remark= db.Column(db.String(20))
    AddUserid=db.Column(db.SmallInteger,nullable=False)
    AddTime = db.Column(db.DateTime, default=datetime.now())
    EditTime = db.Column(db.DateTime, default=datetime.now())
    EditUserid=db.Column(db.SmallInteger,nullable=False)
    Status = db.Column(db.SmallInteger,default=1)
    # 反向引用, Role表中有属性users， User类中有role这个属性;
    # Users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role %s>" % (self.name)

class User(db.Model):
    __tablename__ = "SysUsers"
    Id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(30), unique=True, index=True, nullable=False)  # unique=True用户名不能重复,index 自增 nullable 是否可空
    PassWord = db.Column(db.String(20), nullable=False)
    RealName = db.Column(db.String(20), unique=False)
    Email = db.Column(db.String(20), unique=True)
    Mobile= db.Column(db.String(11), unique=False)
     # 1-男 2-女
    Gender = db.Column(db.SmallInteger,default=2)
    Salt= db.Column(db.String(4), unique=False)
    IsOnLine= db.Column(db.SmallInteger,default=0)
    LastTime= db.Column(db.DateTime, default=datetime.now())
    LastIp= db.Column(db.String(20), unique=False)
    Portrait= db.Column(db.String(200), unique=False)
    # 设置默认值， 位当前用户的创建时间;
    AddUserid=db.Column(db.SmallInteger,nullable=False)
    AddTime = db.Column(db.DateTime, default=datetime.now())
    EditTime = db.Column(db.DateTime, default=datetime.now())
    EditUserid=db.Column(db.SmallInteger,nullable=False)
    Status = db.Column(db.SmallInteger,default=1)
    #### 重要的： 用户角色id不能随便设置， 需要从Role中查询, （外键关联）
    # RoleId = db.Column(db.Integer, db.ForeignKey('sysRole.id'))

    # 定义了 __repr()__ 方法,返回一个具有可读性的字符串表示模型,可在调试和测试时使用。
    def __repr__(self):
        return "<User %s>" % (self.UserName)

class UserBelong(db.Model):
    __tablename__ = "SysUserBelongs"
    # id号递增autoincrement=True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId=db.Column(db.SmallInteger,nullable=False)
    Belongid=db.Column(db.SmallInteger,nullable=False)
    BelongType=db.Column(db.SmallInteger,nullable=False)
    AddUserId=db.Column(db.SmallInteger,nullable=False)
    AddTime = db.Column(db.DateTime, default=datetime.now())
    EditTime = db.Column(db.DateTime, default=datetime.now())
    EditUserId=db.Column(db.SmallInteger,nullable=False)
    Status = db.Column(db.SmallInteger,default=1)
    # 反向引用, Role表中有属性users， User类中有role这个属性;
    # Users = db.relationship('User', backref='Roles')

    def __repr__(self):
        return "<UserBelong %s>" % (self.UserId)

