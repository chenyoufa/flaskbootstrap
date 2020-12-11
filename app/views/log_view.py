from flask import render_template,request,jsonify
from app import curre_app,db
from app.models import User,Menus,to_json
from app.forms  import menu_form
from utils.AllDecorator import route



#菜单首页
@route("/cms/Log/Index")
def MenunIndex():
    return render_template('cms/MenunIndex.html')