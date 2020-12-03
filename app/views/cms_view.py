# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template,request,json,jsonify,redirect,url_for,flash,current_app
from app import app,db
from app.models import User,Menus,to_json
from utils import ImageCode as ImageCodeHelper ,commom,ServerInfo,AllDecorator
from flask import make_response,session
from io import BytesIO
from datetime import datetime
import  config
from werkzeug.security import generate_password_hash,check_password_hash
from app.forms  import menu_form,login_form

app.secret_key = 'please-generate-a-random-secret_key'

 
######################后台###################################


# 递归方式 
def sum_recu(n,outlist): 
    for item in n:
        menusPageObj = Menus.query.filter_by(ParentId=item.Id)
        outlist.append(item)
        sum_recu(menusPageObj,outlist)
    return outlist
#首页
@app.route('/cms/index')
@AllDecorator.is_login
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
