from flask import render_template,request,jsonify
from app import curre_app,db
from app.models import User,SysLog,to_json
from app.forms  import menu_form
from utils.AllDecorator import permission_required,is_login
from sqlalchemy import desc,asc

curre_app.secret_key = 'please-generate-a-random-secret_key'


#日志首页|授权访问
@curre_app.route("/cms/LogIndex")
@permission_required()
def LogIndex():
    return render_template('cms/LogIndex.html')

#分页|搜索|排序
@curre_app.route("/cms/GetLogListJson", methods=['GET'])
def GetLogListJson():
    page = request.args.get("pageIndex", type=int)
    per_page = request.args.get("pageSize", type=int)
    userName = request.args.get("UserName")
    ipAddress = request.args.get("IpAddress")
    startTime = request.args.get("StartTime")
    endTime = request.args.get("EndTime")
    sort = request.args.get("sort")
    sortType = request.args.get("sortType")

    data={'Tag': 0,"Message":"","Data":"","Total":0}
    data["Tag"]=1
    data["Message"]="操作成功"
    logs=SysLog.query.join(User,SysLog.CreateUserid==User.Id).with_entities(
        SysLog.Id.label('Id'),
        User.UserName,
        SysLog.IpAddress,
        SysLog.IpLocation,
        SysLog.Browser,
        SysLog.OS,
        SysLog.LogType,
        SysLog.ExecuteUrl,
        SysLog.ExecuteResult,
        SysLog.ExecuteParam,
        SysLog.Status,
        SysLog.CreateTime,
        SysLog.Remark
    )
    if len(userName)>0:
        logs=logs.filter(User.UserName.contains(userName))
    if len(ipAddress)>0:
        logs=logs.filter(SysLog.IpAddress.contains(ipAddress))
    if len(startTime)>0:
        logs=logs.filter(db.cast(SysLog.CreateTime, db.DATE)>=db.cast(startTime, db.DATE))
    if len(endTime)>0:
        logs=logs.filter(db.cast(SysLog.CreateTime, db.DATE)<=db.cast(endTime, db.DATE))
    if len(sort)>0:
        if sortType=="asc":
            logs=logs.order_by(asc(str(sort)))
        else:
            logs=logs.order_by(desc(str(sort)))

    logs_length=logs.count()
    logs=logs.paginate(page=page,per_page=per_page)
    data["Total"]=logs_length
    data["Data"]=logs.items
    return jsonify(data)

#批量删除
@curre_app.route("/cms/DeleteLogJson", methods=['POST'])
def DeleteLogJson():
    data={'Tag': 0,"Message":"","Data":""}
    _idarr=[]
    _category=0
    try:
        _ids=request.form["ids"]
        _idarr = _ids.split(',')
        _category=request.form["category"]
    except:
        print(exec)
    if len(_idarr)>0:
        data["Tag"]=1
        data["Message"]="操作成功"
        if _category==0:
            logs_del = SysLog.query.filter(SysLog.Id.in_(_idarr)).all()
            
        else:
            logs_del = SysLog.query.all()
        [db.session.delete(u) for u in logs_del]
        db.session.commit()
    return jsonify(data)
