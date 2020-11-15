

# peewee转dict
def obj_to_dict(obj, exclude=None):
    dict = obj.__dict__['_data']
    if exclude:
        for key in exclude:
            if key in dict: dict.pop(key)
    return dict
# peewee转list
def query_to_list(query, exclude=None):
    list = []
    for obj in query:
        print(obj)
        dict = obj_to_dict(obj, exclude)
        list.append(dict)
    return list