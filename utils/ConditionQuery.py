from datetime import datetime
def queryList(**kwargs):
    """
    parameter:
    x1={User.UserName:username},
    x2={User.Mobile:userphone},
    x3={User.Status:userstatus},
    x4={User.ModifyTime:[StartTime,EndTime]
    """

    filterlist = []
    for item in kwargs:
        for k in kwargs[item]:
            if "ModifyTime"  in str(k):
                if kwargs[item][k][0]:
                    filterlist.append(k >= kwargs[item][k][0])
                if kwargs[item][k][1]:
                    filterlist.append(k <= kwargs[item][k][1])
            elif kwargs[item][k] and kwargs[item][k]!="-1":
                filterlist.append(k.like('%'+kwargs[item][k]+'%'))
    return filterlist


def List_to_dicList(QueryList,menu):
    """
    parameter:
    QueryList:Column name to query,example:QueryList=[Id,Username]
    menu:Query results
    """
    tempList = []
    for row in menu:
        tempdic = {}
        for (i, t) in zip(QueryList, row):
            if type(t) is type(datetime.now()):
                t = str(t)
            tempdic[str(i).split(".")[1]] = t
        tempList.append(tempdic)
    return tempList