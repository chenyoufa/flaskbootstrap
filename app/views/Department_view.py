from flask import render_template,jsonify,request
from sqlalchemy import func

from app import curre_app,db
from app.models import Department,User
from utils import ConditionQuery
from app.forms  import depart_form
from datetime import datetime
@curre_app.route('/cms/DepartmentIndex')
def DepartmentIndex():
    return render_template('cms/DepartmentIndex.html')

@curre_app.route('/cms/GetDepartmentListJson')
def GetDepartmentListJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        DepartName = request.args.get("DepartmentName")
        filterList = ConditionQuery.queryList(x1={Department.DepartName:DepartName})
        QueryList = [Department.Id,Department.CreateUserid,Department.CreateTime,Department.ModifyTime,
                     Department.Status,Department.DepartName,User.UserName]
        menu = Department.query.join(User,User.Id == Department.User_id).\
            with_entities(*QueryList).filter(*filterList).all()
        tempList = ConditionQuery.List_to_dicList(QueryList,menu)
        data["Data"] = tempList
    return jsonify(data)

@curre_app.route('/cms/DepartmentFrom')
def DepartmentFrom():
    return render_template("cms/DepartmentForm.html")

@curre_app.route('/cms/GetDepartmentTwoJson')
def GetDepartmentTwoJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        QueryList = [Department.Id,Department.DepartName]
        menu = Department.query.with_entities(*QueryList).all()
        tempList = ConditionQuery.List_to_dicList(QueryList, menu)
        for item in tempList:
            item["name"] = item.pop("DepartName")
            item["id"] = item.pop("Id")
        data["Data"] = tempList
    return jsonify(data)

@curre_app.route('/cms/GetUserTwoJson')
def GetUserTwoJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        QueryList = [User.Id,User.RealName]
        menu = User.query.with_entities(*QueryList).all()
        tempList = ConditionQuery.List_to_dicList(QueryList, menu)
        for item in tempList:
            item["name"] = item.pop("RealName")
            item["id"] = item.pop("Id")
        data["Data"] = tempList
    return jsonify(data)

@curre_app.route('/cms/GetDepartFormJson')
def GetDepartFormJson():
    id = request.args.get("id")
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        QueryList = [Department.Id, Department.CreateUserid, Department.CreateTime, Department.ModifyTime,Department.ModifyUserid,
                     Department.Status, Department.DepartName,Department.ParentId,Department.DepartSort ,Department.Email,User.UserName,
                     Department.Fax,Department.Mobile,Department.Remarks,Department.User_id]
        menu = Department.query.join(User, User.Id == Department.User_id). \
            with_entities(*QueryList).filter(Department.Id == id).all()
        tempList = ConditionQuery.List_to_dicList(QueryList, menu)
        tempList[0]["PrincipalId"] = tempList[0].pop("User_id")
        data["Data"] = tempList[0]
        data["Total"] = 0
    return jsonify(data)

@curre_app.route('/cms/GetDepartMaxSortJson',methods=['GET'])
def GetDepartMaxSortJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        menu = db.session.query(func.max(Department.DepartSort)).scalar()
        data["Data"] = menu + 1
    return jsonify(data)


@curre_app.route('/cms/SaveDepartFormJson', methods=['POST'])
def SaveDepartFormJson():
    form = depart_form.DepartForm()
    data = {'Tag': 0, "Message": ""}
    print(form.validate_on_submit())
    if form.validate_on_submit():
        data["Tag"] = 1
        data["Message"] = "操作成功"
        print("@@@@@@")
        if form.Id.data>0:
            print("修改")
            menu = Department.query.get(form.Id.data)
            menu.ParentId = form.ParentId.data
            menu.DepartName = form.DepartName.data
            menu.User_id = form.PrincipalId.data
            menu.Mobile = form.Mobile.data
            menu.Fax = form.Fax.data
            menu.Email = form.Email.data
            menu.Remarks = form.Remarks.data
            menu.DepartSort = form.DepartSort.data
            menu.ModifyTime = datetime.now()


        else:
            menu = Department(ParentId=form.ParentId.data, DepartName=form.DepartName.data,
                              User_id=form.PrincipalId.data,Mobile=form.Mobile.data, Fax=form.Fax.data,
                              Email=form.Email.data,Remarks=form.Remarks.data,DepartSort=form.DepartSort.data,
                              CreateTime=datetime.now(),ModifyUserid=1,CreateUserid=1)
            db.session.add(menu)
        db.session.commit()

    return jsonify(data)

@curre_app.route("/cms/DeleteDepartJson",methods=['GET','POST'])
def DeleteDepartJson():
    if request.method == "POST":
        data = {'Tag': 0, "Message": "", "Data": ""}
        id = request.form["ids"]
        print(id)
        if id != '':
            data["Tag"] = 1
            data["Message"] = "操作成功"
            menu= Department.query.get(id)
            db.session.delete(menu)
            db.session.commit()
    return jsonify(data)

