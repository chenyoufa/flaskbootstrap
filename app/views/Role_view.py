
from flask import render_template
from app import app,db
from app.models import User,Menus,to_json
from flask import make_response,session
from app.forms  import menu_form,login_form

app.secret_key = 'please-generate-a-random-secret_key'

######################角色 ######################
# 
@app.route("/cms/RoleIndex")
def RoleIndex():
    return render_template('cms/RoleIndex.html')

@app.route("/cms/GetRoleListJson", methods=['GET'])
def GetRoleListJson():
    data={'Tag': 0,"Message":"","Data":""}
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        menu=Role.query.all()
        data["Data"]=menu
    return jsonify(data)
 ############################角色 ######################