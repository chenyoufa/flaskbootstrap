# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template,request,json,jsonify
from app import app
from app.models import User,Menus,to_json
from utils import ImageCode as ImageCodeHelper ,commom
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

#登录
@app.route('/cms/login')
def login():
    """Renders the about page."""
    return render_template(
        'cms/login.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
#首页
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
    
#列表分页
@app.route("/cms/menus/<int:page>",methods=['GET','POST'])
def testlist(page=1):
    Users = User.query.order_by(User.Id.asc()).paginate(page=page,per_page=10)
    return render_template('cms/menus.html', infos=Users.items,pagination=Users)


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
 



 

