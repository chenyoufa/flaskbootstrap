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

def route(*args, **kwargs):
    def wrapper(fun):
        @curre_app.route(endpoint=str(uuid.uuid4()), *args, **kwargs)
        def inner():
            fun()
            permission=request.url.replace(request.host,'').replace("https://","").replace("http://","")
            inslog()
            return fun()
        return inner
    return wrapper

 
def inslog():
    user = session.get('logged_in')
    ip = request.remote_addr
    url=request.url
    method=request.method
    args=request.args.to_dict()
    headers=request.headers
    Agent=headers["User-Agent"]
    u = SysLog(CreateUserid=1,ModifyUserid=1,UserId=1, IpAddress=ip,IpHome='', AgentBrowser=Agent,OperatingSystem='',
    OperationMethod=method,LogCategory=2,OperatingInfo=url,TimeConsue=0,Parameter=str(args))
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