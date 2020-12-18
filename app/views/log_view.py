from flask import render_template,request,jsonify
from app import curre_app,db
from app.models import User,SysLog,to_json
from app.forms  import menu_form
from utils.AllDecorator import route

@route("/cms/LogIndex")
def LogIndex():
    return render_template('cms/LogIndex.html')

#菜单新增修改页面
@route("/cms/LogForm")
def LogForm():
    return render_template('cms/LogForm.html')
 
@route("/cms/GetLogListJson", methods=['GET'])
def GetLogListJson():
    data={'Tag': 0,"Message":"","Data":""}
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"

        # logs=SysLog.query.with_entities(
        #     SysLog.Id.label('Id'),
        #     SysLog.IpAddress,
        #     SysLog.IpHome,
        #     SysLog.AgentBrowser,
        #     SysLog.OperatingSystem,
        #     SysLog.LogCategory,
        #     SysLog.OperatingInfo,
        #     SysLog.OperationMethod,
        #     SysLog.Parameter,
        #     SysLog.Status,
        #     SysLog.CreateTime
        # ).all()

        logs=SysLog.query.with_entities(
            SysLog.Id.label('Id'),
            SysLog.IpAddress,
            SysLog.IpHome,
            SysLog.AgentBrowser,
            SysLog.OperatingSystem,
            SysLog.LogCategory,
            SysLog.OperatingInfo,
            SysLog.OperationMethod,
            SysLog.Parameter,
            SysLog.Status,
            SysLog.CreateTime
        ).all()
        subqry = db.session.query(SysLog)

        data["Data"]=logs
    return jsonify(data)

@route("/cms/AddLogJson", methods=['POST'])
def AddLogJson():
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

@route("/cms/DeleteLogJson", methods=['POST'])
def DeleteLogJson():
    data={'Tag': 0,"Message":"","Data":""}
    id=request.form["ids"]
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        logs=SysLog.query.get(id)
        db.session.delete(logs)
        db.session.commit()
    return jsonify(data)
