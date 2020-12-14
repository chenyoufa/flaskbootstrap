from flask import render_template,jsonify,request
from app import curre_app
from app.models import User,to_json,Role,db
from utils import ConditionQuery

@curre_app.route('/cms/UsersIndex')
def UsersIndex():
    return render_template('cms/UsersIndex.html')


@curre_app.route("/cms/GetUsersListJson", methods=['GET'])
def GetUsersListJson():
    data={'Tag': 0,"Message":"","Data":""}
    if id!='':
        data["Tag"]=1
        data["Message"]="操作成功"
        page = request.args.get("pageIndex",type=int)
        per_page = request.args.get("pageSize",type=int)
        username = request.args.get("UserName")
        userphone = request.args.get("UserPhone")
        userstatus =request.args.get("UserStatus")
        StartTime = request.args.get("StartTime")
        EndTime = request.args.get("EndTime")
        filterList = ConditionQuery.queryList(x1={User.UserName:username},x2={User.Mobile:userphone},x3={User.Status:userstatus},x4={User.ModifyTime:[StartTime,EndTime]})
        menu1=User.query.filter(*filterList)
        menu=menu1.paginate(page,per_page)
        data["Total"]=menu.pages
        data["Data"]=to_json(menu.items)
    return jsonify(data)

@curre_app.route("/cms/UserForm")
def UserForm():
    return render_template("cms/UserForm.html")

@curre_app.route("/cms/GetRoleJson")
def GetRoleJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    id = request.args.get("id")
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        QueryList=[Role.Id,Role.Name]
        RoleList=Role.query.filter(User.Id==id).with_entities(*QueryList).all()
        data["Data"] = ConditionQuery.List_to_dicList(QueryList,RoleList)

        return jsonify(data)


@curre_app.route("/cms/GetUserFormJson")
def GetUserFormJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    id = request.args.get("id")
    print(id)
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        menu = User.query.filter(User.Id == id).all()
        print(menu)
        data["data"] = to_json(menu)[0]
    return jsonify(data)

@curre_app.route("/cms/DeleteUserJson",methods=['GET','POST'])
def DeleteUserJson():
    if request.method == "POST":
        data = {'Tag': 0, "Message": "", "Data": ""}
        id = request.form["ids"]
        if id != '':
            data["Tag"] = 1
            data["Message"] = "操作成功"
            menu= User.query.get(id)
            db.session.delete(menu)
            db.session.commit()
    return jsonify(data)