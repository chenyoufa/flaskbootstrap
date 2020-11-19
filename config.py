import datetime
#线上数据库链接
# SQLALCHEMY_DATABASE_URI = 'mysql://mytest:123456@192.168.1.17:25481/mytest'
#本地数据库链接
SQLALCHEMY_DATABASE_URI = 'mysql://mytest:123456@192.168.1.17/mytest'
SQLALCHEMY_TRACK_MODIFICATIONS = True

#获取web运行开始时间
filename = 'test.txt'
with open(filename, 'w') as file_object:
    file_object.write(str(datetime.datetime.now()))
