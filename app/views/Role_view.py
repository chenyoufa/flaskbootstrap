
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
        menu=Menus.query.all()
        data["Data"]=menu
    return jsonify(data)
 ############################角色 ######################