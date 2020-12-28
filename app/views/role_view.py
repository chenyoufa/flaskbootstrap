
from flask import render_template,request
from app import curre_app,db
from app.models import User,Role
from flask import jsonify,session
from app.forms  import role_form
from sqlalchemy import desc,asc
from datetime import datetime
#角色首页
@curre_app.route("/cms/RoleIndex")
def RoleIndex():
    return render_template('cms/RoleIndex.html')
#角色首页列表数据获取
@curre_app.route("/cms/GetRoleListJson", methods=['GET'])
def GetRoleListJson():
    page = request.args.get("pageIndex", type=int)
    per_page = request.args.get("pageSize", type=int)
    roleName = request.args.get("RoleName")
    roleStatus = request.args.get("RoleStatus")
    startTime = request.args.get("StartTime")
    endTime = request.args.get("EndTime")
    sort = request.args.get("sort")
    sortType = request.args.get("sortType")
    data={'Tag': 0,"Message":"","Data":"","Total":0}
    data["Tag"]=1
    data["Message"]="操作成功"
    roles=Role.query.with_entities(Role.Id.label('Id'),
        Role.Name.label('RoleName'),
        Role.Sort.label('RoleSort'),
        Role.Status.label('RoleStatus'),
        Role.ModifyTime.label('BaseModifyTime'),
        )
    if len(roleName)>0:
        roles=roles.filter(Role.Name.contains(roleName))
    if len(roleStatus)>0 and roleStatus!="-1":
        print("roleStatus:",roleStatus)
        roles=roles.filter(Role.Status==int(roleStatus))
    if len(startTime)>0:
        roles=roles.filter(db.cast(Role.CreateTime, db.DATE)>=db.cast(startTime, db.DATE))
    if len(endTime)>0:
        roles=roles.filter(db.cast(Role.CreateTime, db.DATE)<=db.cast(endTime, db.DATE))
    if len(sort)>0:
        if sortType.lower()=="asc":
            roles=roles.order_by(asc(str(sort)))
        else:
            roles=roles.order_by(desc(str(sort)))

    roles_length=roles.count()
    roles=roles.paginate(page=page,per_page=per_page)
    data["Total"]=roles_length
    data["Data"]=roles.items
    return jsonify(data)
#角色维护
@curre_app.route("/cms/RoleForm")
def RoleForm():
    return render_template('cms/RoleForm.html')

@curre_app.route("/cms/SaveRoleFormJson", methods=['POST'])
def SaveRoleFormJson():
    form =role_form.RoleForm()  
    data={'Tag': 0,"Message":""}
    if form.validate_on_submit():
        try:
            if form.Id.data<=0:

               
                role = Role( Name=form.RoleName.data,
                Sort=form.RoleSort.data,Remark=form.Remark.data,
                Status=form.RoleStatus.data,CreateUserid=session.get('User_Id'))
                
                db.session.add(role)
            else:
                role=Role.query.get(form.Id.data)

                role.Name=form.RoleName.data
                role.Sort =form.RoleSort.data
                role.Remark=form.Remark.data
                role.Status=form.RoleStatus.data
                role.ModifyTime=datetime.now
                role.ModifyUserid=session.get('User_Id')

            db.session.commit()
            data["Tag"]=1
            data["Message"]="操作成功"
        except Exception as err:
            data["Tag"]=-1
            data["Message"]="异常，请刷新页面重新试试"+str(err)
    else:
           data["Message"] =  form.errors.popitem()[0]+" "+form.errors.popitem()[1][0]
    return jsonify(data)

#角色维护数据获取
@curre_app.route("/cms/GetRoleFormJson", methods=['GET'])
def GetRoleFormJson():
    data={'Tag': 0,"Message":"","Data":""}
    id=request.args.get("id")
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        roles=Role.query.with_entities(
            Role.Id,
            Role.Name.label("RoleName"),
            Role.Sort.label("RoleSort"),
            Role.Status.label("RoleStatus"),
            Role.Remark,
        ).filter_by(Id=id)
    
        if roles.count()>0:
            data["Data"]=roles[0] 
    return jsonify(data)

#角色单条删除|批量删除
@curre_app.route("/cms/DeleteRoleJson", methods=['POST'])
def DeleteRoleJson():
    data={'Tag': 0,"Message":"","Data":""}
    _idarr=[]
    try:
        _ids=request.form["ids"]
        _idarr = _ids.split(',')
    except:
        print(exec)
    if len(_idarr)>0:
        data["Tag"]=1
        data["Message"]="操作成功"
        roles_del = Role.query.filter(Role.Id.in_(_idarr)).all()
        
        [db.session.delete(u) for u in roles_del]
        db.session.commit()
    return jsonify(data)
