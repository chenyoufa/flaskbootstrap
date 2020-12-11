from flask import render_template,jsonify,request
from app import app,db
from app.models import Department,to_json,Role,User
from utils import ConditionQuery

@app.route('/cms/DepartmentIndex')
def DepartmentIndex():
    return render_template('cms/DepartmentIndex.html')

@app.route('/cms/GetDepartmentListJson')
def GetDepartmentListJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        DepartName = request.args.get("DepartmentName")
        filterList = ConditionQuery.queryList(x1={Department.DepartName:DepartName})
        QueryList = [Department.Id,Department.CreateUserid,Department.CreateTime,Department.ModifyTime,Department.Status,Department.DepartName,User.UserName]
        menu = Department.query.join(User,User.Id == Department.User_id).\
            with_entities(*QueryList).filter(*filterList).all()
        tempList = ConditionQuery.List_to_dicList(QueryList,menu)
        data["Data"] = tempList
    return jsonify(data)

@app.route('/cms/DepartmentFrom')
def DepartmentFrom():
    return render_template("cms/DepartmentForm.html")

@app.route('/cms/GetDepartmentTwoJson')
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
        print(tempList)
        data["Data"] = tempList
    return jsonify(data)

@app.route('/cms/GetUserTwoJson')
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
        data["Data"] = tempList
    return jsonify(data)

@app.route('/cms/GetDepartFormJson')
def GetDepartFormJson():
    id = request.args.get("id")
    print(id)
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        menu = Department.query.filter(Department.Id == id).all()
        data["Data"] = to_json(menu)[0]
        data["Total"] = 0
    return jsonify(data)