from flask import render_template,jsonify,request
from app import app,db
from app.models import Department,to_json,Role,User
from utils import ConditionQuery
from app.forms  import depart_form

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
            item["id"] = item.pop("Id")
            # item["pId"] = item["id"]
        # print(tempList)
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
            item["id"] = item.pop("Id")
        data["Data"] = tempList
    return jsonify(data)

@app.route('/cms/GetDepartFormJson')
def GetDepartFormJson():
    id = request.args.get("id")
    # print(id)
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        menu = Department.query.filter(Department.Id == id).all()
        data["Data"] = to_json(menu)[0]
        data["Total"] = 0
    return jsonify(data)

@app.route('/cms/SaveDepartFormJson', methods=['POST'])
def SaveDepartFormJson():
    form = depart_form.DepartForm()
    data = {'Tag': 0, "Message": ""}
    print("-------------------")
    print(form.validate_on_submit())
    if form.validate_on_submit():

        data["Tag"] = 1
        data["Message"] = "操作成功"
        print("@@@@@@")
        # print(form.ParentId.data)
        print(form.ParentId.data,form.DepartName.data,form.Mobile.data,form.Fax.data,form.Email.data,form.Remarks.data,form.DepartSort.data)
        # menu = Department.query.get(form.Id.data)
        # menu.ParentId = form.ParentId.data
        # menu.DepartName = form.DepartName.data
        # # menu.User_id = form.User_id.data
        # menu.Mobile = form.Mobile.data
        # menu.Fax = form.Fax.data
        # menu.Email = form.Email.data
        # menu.Remarks = form.Remarks.data
        # menu.DepartSort = form.DepartSort.data
        # print(menu)
    # else:
    #     print(form.Id.data,"@@@@")
    # id = request.form ["Id"]
    # if request.method == "POST":
    #     if int(id) > 0 :
    #         data["Tag"] = 1
    #         data["Message"] = "操作成功"
    #         parentId = request.form["ParentId"]
    #         departName = request.form["DepartName"]
    #         principalId = request.form["PrincipalId"]
    #         mobile = request.form["Mobile"]
    #         fax = request.form["Fax"]
    #         email = request.form["Email"]
    #         departSort = request.form["DepartSort"]
    #         remarks = request.form["Remarks"]
    #         print(id,parentId,departName,principalId,mobile,fax,email,departSort,remarks)
    #     else:
    #         print("add")
    return jsonify(data)