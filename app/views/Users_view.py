from flask import render_template,jsonify,request
from app import app
from app.models import User,to_json

def queryList(**kwargs):
    filterlist = []
    for item in kwargs:
        for k in kwargs[item]:
            if kwargs[item][k] and kwargs[item][k]!=-1:
                filterlist.append(k.like('%'+kwargs[item][k]+'%'))

    return filterlist



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
        username = request.args.get("UserName")
        userphone = request.args.get("UserPhone")
        userstatus =request.args.get("UserStatus")
        filterList = queryList(x1={User.UserName:username},x2={User.Mobile:userphone},x3={User.Status:userstatus})
        print(filterList)
        menu1=User.query.filter(*filterList)
        menu=menu1.paginate(int(page),int(per_page))
        # print(menu.pages)
        data["Total"]=menu.pages
        data["Data"]=to_json(menu.items)
    return jsonify(data)