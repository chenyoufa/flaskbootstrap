# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template,request,json,jsonify,redirect,url_for
from app import app
from app.models import User,Menus,to_json
from utils import ImageCode as ImageCodeHelper ,commom,ServerInfo,LoginDecorator
from flask import make_response,session
from io import BytesIO
from datetime import datetime
import  config
from werkzeug.security import generate_password_hash,check_password_hash

 
app.secret_key = 'please-generate-a-random-secret_key'

 
######################后台###################################
# 递归方式 
def sum_recu(n,outlist): 
    for item in n:
        menusPageObj = Menus.query.filter_by(ParentId=item.Id)
        outlist.append(item)
        sum_recu(menusPageObj,outlist)
    return outlist

#哈希加盐的密码加密方法
def enPassWord(password):#将明密码转化为hash码
    return generate_password_hash(password)#返回转换的hash码

def checkPassWord(enpassword,password):#第一参数是从数据查询出来的hash值，第二参数是需要检验的密码
    return check_password_hash(enpassword,password)#如果匹配返回true

def isNameExisted(username):#检查名字是否存在
    result = User.query.filter(User.UserName == username).first()
    # print(result)
    if (result == None ):
        return False
    else:
        return True,result.PassWord



#登录
@app.route('/cms/login',methods=['GET', 'POST'])
def login():
    """Renders the about page."""
    if request.method == "GET":
        return render_template(
            'cms/login.html',
            title='About',
            year=datetime.now().year,
            message='Your application description page.'
        )
    if request.method == "POST":
        userName = request.form["userName"]
        password = request.form["password"]
        captchaCode = request.form["captchaCode"]

        if isNameExisted(userName):
            s,t= isNameExisted(userName)
            if check_password_hash(t, password) and session['imageCode'].lower() == captchaCode.lower() :  # 查询有没有这个用户
                session['logged_in'] = userName
                index_url = url_for('index')
                return redirect(index_url)

            else:  # 没有用户就是新用户那么就转入注册页面
                return redirect('/cms/login')
#注销页
@app.route("/cms/login_out")
def login_out():
    session.clear()
    index_url = url_for('login')
    return redirect(index_url)



#首页
@app.route('/cms/index')
@LoginDecorator.is_login
def index():
    menusPageObj = Menus.query.filter_by(ParentId=0)
    outlist=[]
    sum_recu(menusPageObj,outlist) 
    """Renders the about page."""
    return render_template(
        'cms/index.html',
        username = session["logged_in"],
        infos=outlist,
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
    
#列表分页
@app.route("/cms/menus/<int:page>",methods=['GET','POST'])
def testlist(page=1):
    Users = User.query.order_by(User.Id.asc()).paginate(page=page,per_page=10)
    return render_template('cms/menus.html', infos=Users.items,pagination=Users)

@app.route("/cms/MenuIndex")
def Menundex():
    return render_template('cms/MenuIndex.html')

@app.route('/cms/GetTestListJson', methods=['GET'])
def GetTestListJson(page=1):
   
    if request.method == 'POST':
        print('post')
    if request.method == 'GET':
        menus = Menus.query.paginate(page=page,per_page=10)
        # users = User.query.all()
        # print(users.single_to_dict()) 
        return jsonify(to_json(menus.items))

        # return jsonify({'total': query.items})
        # 注意total与rows是必须的两个参数，名字不能写错，total是数据的总长度，rows是每页要显示的数据,它是一个列表
        # 前端根本不需要指定total和rows这俩参数，他们已经封装在了bootstrap table里了
        #{'total': len(data.items), 'rows': data.items}
 

@app.route('/cms/SeverInfo/',methods=['GET'])
def GetServerInfo():
    size_cpu,used_cpu  = ServerInfo.serverinfo().get_cpu_info()
    size_memory,used_memory  = ServerInfo.serverinfo().get_memory_info()
    host_name  = ServerInfo.serverinfo().get_hostname_info()
    System_version,system_framework  = ServerInfo.serverinfo().get_system_info()
    out_ip,in_ip  = ServerInfo.serverinfo().get_ip_info()
    run_time  = ServerInfo.serverinfo().get_system_runtime()
    web_starttime,web_runtime = ServerInfo.serverinfo().get_web_runtime()
    flask_version,web_path,flask_env,python_version = ServerInfo.serverinfo().get_flask_info()
    context = {
        "size_cpu":size_cpu,
        "used_cpu":used_cpu,
        "size_memory":size_memory,
        "used_memory":used_memory,
        "host_name":host_name,
        "System_version":System_version,
        "out_ip":out_ip,
        "in_ip":in_ip,
        "run_time":run_time,
        "system_framework":system_framework,
        "web_runtime":web_runtime,
        "web_starttime":web_starttime,
        "flask_version":flask_version,
        "web_path":web_path,
        "flask_env":flask_env,
        "python_version":python_version

    }
    return render_template("cms/SeverIndex.html",**context)