from flask import session,redirect,abort,request
from app import curre_app,db
from functools import wraps
import uuid
from app.models import SysLog
#装饰器的方法
def is_login(func):
    @wraps(func)
    def inner(*args,**kwargs):
        user = session.get('logged_in')
        if not user:
            return redirect('login')
        return func(*args,**kwargs)
    return inner

def AuthorizeFilter(func):
    @wraps(func)
    def inner(*args,**kwargs): 
        # permission=request.url.replace(request.host,'').replace("https://","").replace("http://","")
        # print("permission:",permission)
        inslog()
        return func(*args,**kwargs)
    return inner

from user_agents import parse

def inslog():
    user = session.get('User_Id')
    url=request.url
    ip = request.remote_addr
    url=request.url
    method=request.method
    args=request.args.to_dict()
    headers=request.headers
    ua_string=headers["User-Agent"]
    user_agent = parse(ua_string)  # 解析成user_agent
    bw = user_agent.browser.family  # 判断是什么浏览器
    os = user_agent.os.family  # 判断是什么操作系统
    print("os:",os)
    u = SysLog(CreateUserid=user,ModifyUserid=1,IpAddress=ip,
    Browser=bw,OS=os,ExecuteUrl=url,ExecuteParam=str(args))
    db.session.add(u)
    db.session.commit()

# def permission_can(current_user, permission):
#     """
#     检测用户是否有特定权限
#     :param current_user
#     :param permission
#     :return:
#     """
#     role_id = current_user.role_id
#     role = db.session.query(Role).filter_by(id=role_id).first()
#     return (role.permissions & permission) == permission


# def permission_required():
#     """
#     权限认证装饰器
#     :param permission:
#     :return:
#     """
    
#     def decorator(f):
#         @wraps(f)
#         def decorated_function(*args, **kwargs):
#             try:
#                 permission=request.url.replace(request.host,'').replace("https://","").replace("http://","")
#                 current_user = Users.query.filter_by(id=session.get('logged_in')).first()
                
#                 if not current_user and permission_can(current_user, permission):
#                     abort(403)
#                 return f(*args, **kwargs)
#             except:
#                 abort(403)
#         return decorated_function
#     return decorator