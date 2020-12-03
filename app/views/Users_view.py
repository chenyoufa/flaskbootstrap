from flask import render_template,jsonify,request
from app import app
from app.models import User,to_json
import json



@app.route('/cms/UsersIndex')
def UsersIndex():
    return render_template('cms/UsersIndex.html')

# def to_json(all_vendors):
#     v = [ ven.dobule_to_dict() for ven in all_vendors ]
#     return v

@app.route("/cms/GetUsersListJson", methods=['GET'])
def GetUsersListJson():
    data={'Tag': 0,"Message":"","Data":""}
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        page = request.args.get("pageIndex")
        per_page = request.args.get("pageSize")
        menu=User.query.paginate(int(page),int(per_page)).items
        data["Data"]=to_json(menu)
    return jsonify(data)