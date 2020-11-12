# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template
from app import app
from app.models import User,Menus
import utils.ImageCode as ImageCodeHelper 
from flask import make_response,session
from io import BytesIO
from datetime import datetime
app.secret_key = 'please-generate-a-random-secret_key'

 
######################后台###################################
# 递归方式 
def sum_recu(n,outlist): 
    for item in n:
        menusPageObj = Menus.query.filter_by(ParentId=item.Id)
        outlist.append(item)
        sum_recu(menusPageObj,outlist)
    return outlist

@app.route('/cms/login')
def login():
    """Renders the about page."""
    return render_template(
        'cms/login.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/cms/index')
def index():
    menusPageObj = Menus.query.filter_by(ParentId=0)
    outlist=[]
    sum_recu(menusPageObj,outlist) 
    """Renders the about page."""
    return render_template(
        'cms/index.html',
        infos=outlist,
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
    

@app.route("/testlist/<int:page>",methods=['GET','POST'])
def testlist(page=1):
    Users = User.query.order_by(User.Id.asc()).paginate(page=page,per_page=10)
    return render_template('cms/test.html', infos=Users.items,pagination=Users)


 

