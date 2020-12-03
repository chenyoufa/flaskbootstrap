# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template,request,jsonify,redirect,url_for
from app import app,db
from app.models import User
from flask import session
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app.forms  import login_form

app.secret_key = 'please-generate-a-random-secret_key'

 
######################后台###################################


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
         
        form =login_form.LoginForm()
        userName = form.username.data
        password = form.password.data
        captchaCode = form.captchaCode.data


        if isNameExisted(userName):
            s,t= isNameExisted(userName)
            if check_password_hash(t, password):
                if session['imageCode'].lower() == captchaCode.lower() :  # 查询有没有这个用户
                    session['logged_in'] = userName
                    return jsonify({"index_url":"/cms/index","status":200})
                else:
                    erro = "captchaCode is not right "
                    return jsonify({"erros":erro})
                    # print(erro)
                    # return render_template(
                    #     'cms/login.html',
                    #     erros=erro
                    # )

            else:  # 没有用户就是新用户那么就转入注册页面
                erro = "password is not right user"
                return jsonify({"erros":erro})
        else:
            erro = "%s is not right user"%userName
            return jsonify({"erros":erro})
#注销页
@app.route("/cms/login_out")
def login_out():
    session.clear()
    index_url = url_for('login')
    return redirect(index_url)
