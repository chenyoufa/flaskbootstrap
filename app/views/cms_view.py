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
    
@app.route('/list/')
@app.route('/list/<int:page>/')
def list(page=1):
    # # 每页显示的数据
    per_page = 10
    # 返回的是 Pagination对象
    menusPageObj = Menus.query.paginate(page=page, per_page=per_page)
    return render_template('cms/index.html',
                           infos=outlist
                           )
                            # 字典for循环数据
    # return render_template('cms/page.html', students=students)


 

