
from flask import render_template
from app import app,db
from app.models import User,Role,to_json
from flask import make_response,session,jsonify
from app.forms  import menu_form,login_form

app.secret_key = 'please-generate-a-random-secret_key'

######################角色 ######################
# 
@app.route("/cms/RoleIndex")
def RoleIndex():
    return render_template('cms/RoleIndex.html')
@app.route("/cms/RoleForm")
def RoleForm():
    return render_template('cms/RoleForm.html')

@app.route("/cms/GetRoleListJson", methods=['GET'])
def GetRoleListJson():
    data={'Tag': 0,"Message":"","Data":""}
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        role=Role.query.with_entities(Role.Id.label('Id'),
        Role.Name.label('RoleName'),
        Role.Sort.label('RoleSort'),
        Role.Status.label('RoleStatus'),
        Role.ModifyTime.label('BaseModifyTime'),
        ).all()
        data["Data"]=role
    return jsonify(data)

@app.route("/cms/DeleteRoleJson", methods=['POST'])
def DeleteRoleJson():
    data={'Tag': 0,"Message":"","Data":""}
    id=request.form["ids"]
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        role=Role.query.get(id)
        db.session.delete(role)
        db.session.commit()
    return jsonify(data)