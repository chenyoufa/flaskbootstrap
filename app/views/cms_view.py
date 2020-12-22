# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template,session,request
from app.models import User,Menus,to_json
from utils import AllDecorator
from app import curre_app
from datetime import datetime
######################后台###################################
 

# 递归方式 
def sum_recu(n,outlist): 
    for item in n:
        menusPageObj = Menus.query.filter_by(ParentId=item.Id)
        outlist.append(item)
        sum_recu(menusPageObj,outlist)
    return outlist
#首页
@curre_app.route('/cms/index')
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


@curre_app.route('/cms/Skin')
def Skin():
    return render_template("cms/Skin.html")

@curre_app.route('/cms/UserDetail')
def UserDetail():
    return render_template("cms/UserDetail.html")