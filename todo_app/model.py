import web


host='90b514053e09c9c7.c.cloudtogo.cn'
port=38008
db = web.database(dbn='mysql', user='root', pw='123456', db='todo',host='90b514053e09c9c7.c.cloudtogo.cn',port=38008)

def get_todos():
    return db.select("todo", order="id")


def new_todo(text):
    db.insert("todo", title=text)


def del_todo(id):
    db.delete("todo", where="id=$id", vars=locals())