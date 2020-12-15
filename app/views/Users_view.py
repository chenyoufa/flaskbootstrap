from flask import render_template,jsonify,request
from app import curre_app
from app.models import User,to_json,Role,db,Department,Position
from utils import ConditionQuery,EncToDec
from app.forms  import user_form
from  datetime import  datetime
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
        filterList = ConditionQuery.queryList(x1={User.UserName:username},x2={User.Mobile:userphone},
                                              x3={User.Status:userstatus},x4={User.ModifyTime:[StartTime,EndTime]})
        QueryList = [User.Id, User.CreateTime,User.RealName,
                     Department.DepartName,User.Mobile,User.Status, User.UserName]
        menu = User.query.join(Department, User.DepartmentId == Department.Id). \
            with_entities(*QueryList).filter(*filterList).paginate(page,per_page)
        tempList = ConditionQuery.List_to_dicList(QueryList, menu.items)
        data["Total"]=menu.pages
        data["Data"] = tempList
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
        RoleList=Role.query.with_entities(*QueryList).all()
        data["Data"] = ConditionQuery.List_to_dicList(QueryList,RoleList)

        return jsonify(data)


@curre_app.route("/cms/GetUserFormJson")
def GetUserFormJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    id = request.args.get("id")
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        menu = User.query.filter(User.Id == id).all()
        data["Data"] = to_json(menu)[0]
    return jsonify(data)

@curre_app.route("/cms/SavePositionFormJson", methods=['POST'])
def SavePositionFormJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    form = user_form.UserForm()
    if form.validate_on_submit():
        data["Tag"] = 1
        data["Message"] = "操作成功"
        if form.Id.data > 0 :
            menu = User.query.get(form.Id.data)
            menu.UserName = form.UserName.data
            menu.PassWord = EncToDec.enPassWord(form.PassWord.data.strip())
            menu.RealName = form.RealName.data
            menu.Gender = form.Gender.data
            menu.Email = form.Email.data
            menu.Mobile = form.Mobile.data
            menu.DepartmentId = form.DepartmentId.data
            menu.PositionId = form.PositionId.data
            menu.RoleId = form.RoleId.data
            menu.Status = form.Status.data
            menu.Remark = form.Remark.data
            menu.ModifyTime = datetime.now()
        else:
            menu = User(UserName=form.UserName.data,PassWord = EncToDec.enPassWord(form.PassWord.data.strip()),RealName = form.RealName.data,
                        Gender = form.Gender.data,Email = form.Email.data,DepartmentId = form.DepartmentId.data,CreateUserid=1,ModifyUserid=1,
                        PositionId = form.PositionId.data,RoleId = form.RoleId.data,Status = form.Status.data,
                        Remark = form.Remark.data,CreateTime = datetime.now())
            db.session.add(menu)
        db.session.commit()

    return jsonify(data)

@curre_app.route('/cms/GetPositionTwoJson')
def GetPositionTwoJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        QueryList = [Position.Id,Position.PositionName]
        menu = Position.query.with_entities(*QueryList).all()
        tempList = ConditionQuery.List_to_dicList(QueryList, menu)
        # for item in tempList:
        #     # item["name"] = item.pop("PositionName")
        #     # item["id"] = item.pop("Id")
        data["Data"] = tempList
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