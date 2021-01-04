from flask import render_template,request,jsonify
from app import curre_app,db
from app.models import User,Menus,to_json
from app.forms  import menu_form
from utils.AllDecorator import permission_required
######################菜单###################################

#菜单首页
@curre_app.route("/cms/MenunIndex", methods=['GET'])
def MenunIndex():
    return render_template('cms/MenunIndex.html')
#菜单首页json接口
@curre_app.route('/cms/GetMenuListJson', methods=['GET'])
def GetMenuListJson(page=1):
   
    if request.method == 'POST':
        print('post')
    if request.method == 'GET':
        menus = Menus.query.all()
        # users = User.query.all()
        # print(users.single_to_dict()) 
        return jsonify(to_json(menus))

        # return jsonify({'total': query.items})
        # 注意total与rows是必须的两个参数，名字不能写错，total是数据的总长度，rows是每页要显示的数据,它是一个列表
        # 前端根本不需要指定total和rows这俩参数，他们已经封装在了bootstrap table里了
        #{'total': len(data.items), 'rows': data.items}

#菜单新增修改页面
@curre_app.route("/cms/MenuForm")
def MenuForm():
    return render_template('cms/MenuForm.html')
 
@curre_app.route("/cms/GetMenuFormJson", methods=['GET'])
def GetMenuJson():
    data={'Tag': 0,"Message":"","Data":""}
    id=request.args.get("id")
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        menu=Menus.query.get(id)
        menujson=menu.dobule_to_dict()
        parentName='系统'
        if menu.ParentId>0:
            parentName=Menus.query.get(menu.ParentId).MenuName
        menujson["ParentName"]=parentName
        data["Data"]=menujson
    return jsonify(data)

@curre_app.route("/cms/AddMenuJson", methods=['POST'])
def AddMenuJson():
    form =menu_form.MenuForm()
    
    data={'Tag': 0,"Message":""}
    if form.validate_on_submit():
        try:
            if form.Id.data<=0:
                menu = Menus(ParentId=form.ParentId.data,MenuName=form.MenuName.data,MenuIcon=form.MenuIcon.data,MenuUrl=form.MenuUrl.data,MenuType=form.MenuType.data,Authorize=form.Authorize.data,Remark=form.Remark.data,MenuSort=form.MenuSort.data,Status=1,CreateUserid=1,ModifyUserid=1)
                db.session.add(menu)
            else:
                menu=Menus.query.get(form.Id.data)
                menu.ParentId=form.ParentId.data
                menu.MenuName=form.MenuName.data
                menu.MenuIcon=form.MenuIcon.data
                menu.MenuUrl=form.MenuUrl.data
                menu.MenuType=form.MenuType.data
                menu.Authorize=form.Authorize.data
                menu.Remark=form.Remark.data
                menu.MenuSort=form.MenuSort.data
            
            db.session.commit()
            data["Tag"]=1
            data["Message"]="操作成功"
        except Exception as err:
            data["Tag"]=-1
            data["Message"]="异常，请刷新页面重新试试"+str(err)
    else:
           data["Message"] =  form.errors.popitem()[0]+" "+form.errors.popitem()[1][0]
    return jsonify(data)

@curre_app.route("/cms/DeleteMenuJson", methods=['POST'])
def DeleteMenuJson():
    data={'Tag': 0,"Message":"","Data":""}
    id=request.form["ids"]
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        menu=Menus.query.get(id)
        db.session.delete(menu)
        db.session.commit()
    return jsonify(data)


@curre_app.route("/cms/MenuChoose")
def MenuChoose():
    return render_template('cms/MenuChoose.html')
@curre_app.route("/cms/GetMenuTreeListJson", methods=['GET'])
def GetMenuTreeListJson():
    data={'Tag': 0,"Message":"","Data":""}
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        menu=Menus.query.with_entities(Menus.Id.label('id'),Menus.ParentId.label('pId'),Menus.MenuName.label('name')).all()
        data["Data"]=menu
    return jsonify(data)

 ######################菜单###################################
