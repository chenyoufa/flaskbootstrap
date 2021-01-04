from flask import render_template,jsonify,request
from sqlalchemy import func
from datetime import datetime
from app import curre_app,db
from app.models import Position,to_json
from utils import ConditionQuery
from app.forms  import position_form

@curre_app.route('/cms/PositionIndex')
def PositionIndex():
    return render_template('cms/PositionIndex.html')

@curre_app.route('/cms/GetPositionListJson')
def GetPositionListJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    page = request.args.get("pageIndex", type=int)
    per_page = request.args.get("pageSize", type=int)
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        PositionName = request.args.get("PositionName")
        filterList = ConditionQuery.queryList(x1={Position.PositionName: PositionName})
        menu = Position.query.filter(*filterList).paginate(page,per_page)
        data["Total"]=menu.pages
        data["Data"]=to_json(menu.items)
    return jsonify(data)

@curre_app.route('/cms/PositionForm')
def PositionForm():
    return render_template('cms/PositionForm.html')

@curre_app.route('/cms/GetPositionFormJson')
def GetPositionFormJson():
    id = request.args.get("id")
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        QueryList = [Position.Id, Position.PositionName, Position.PositionSort, Position.Status,
                     Position.Remark]
        menu = Position.query.with_entities(*QueryList).filter(Position.Id == id).all()
        tempList = ConditionQuery.List_to_dicList(QueryList, menu)
        tempList[0]["PositionStatus"] = tempList[0].pop("Status")
        data["Data"] = tempList[0]
    return jsonify(data)


@curre_app.route('/cms/GetPositionMaxSortJson',methods=['GET'])
def GetPositionMaxSortJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    if id != '':
        data["Tag"] = 1
        data["Message"] = "操作成功"
        menu = db.session.query(func.max(Position.PositionSort)).scalar()
        data["Data"] = menu + 1
    return jsonify(data)

@curre_app.route('/cms/SavePostionFormJson', methods=['POST'])
def SavePostionFormJson():
    data = {'Tag': 0, "Message": "", "Data": ""}
    form = position_form.PositionForm()
    if form.validate_on_submit():
        data["Tag"] = 1
        data["Message"] = "操作成功"
        if form.Id.data >0:
            menu = Position.query.get(form.Id.data)
            menu.PositionName = form.PositionName.data
            menu.PositionSort = form.PositionSort.data
            menu.Status = form.PositionStatus.data
            menu.Remark = form.Remark.data
            menu.ModifyTime = datetime.now()

        else:
            menu = Position(CreateUserid=1,CreateTime=datetime.now(),ModifyTime=datetime.now(),
                            ModifyUserid=1,Status=form.PositionStatus.data,BaseIsDelete=0,
                            BaseCreatorId=1,BaseModifierId=1,BaseVersion=1,
                            PositionName=form.PositionName.data,PositionSort=form.PositionSort.data,
                            Remark=form.Remark.data)
            db.session.add(menu)
        db.session.commit()
    return jsonify(data)

@curre_app.route('/cms/DeletePositionJson',methods=['GET','POST'])
def DeletePositionJson():
    if request.method == "POST":
        data = {'Tag': 0, "Message": "", "Data": ""}
        id = request.form["ids"]
        if id != '':
            data["Tag"] = 1
            data["Message"] = "操作成功"
            menu= Position.query.get(id)
            db.session.delete(menu)
            db.session.commit()
    return jsonify(data)