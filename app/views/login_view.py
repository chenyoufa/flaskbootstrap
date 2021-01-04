# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template,request,jsonify,redirect,url_for
from app import curre_app,db
from app.models import User
from flask import session
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app.forms  import login_form
from  utils import  EncToDec

curre_app.secret_key = 'please-generate-a-random-secret_key'

 
######################后台###################################


#登录
@curre_app.route('/cms/login',methods=['GET', 'POST'])
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


        if EncToDec.isNameExisted(userName):
            s,t= EncToDec.isNameExisted(userName)
            if EncToDec.check_password_hash(t, password):
                if session['imageCode'].lower() == captchaCode.lower() :  # 查询有没有这个用户
                    menu = User.query.with_entities(User.Id).filter(User.UserName==userName).first()
                    session['logged_in'] = userName
                    session['User_Id'] = menu[0]
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
@curre_app.route("/cms/login_out")
def login_out():
    session.clear()
    index_url = url_for('login')
    return redirect(index_url)
