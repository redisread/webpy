import web

# 指定模板目录
render = web.template.render('templates')

db = web.database(dbn='mysql', user='root', pw='123456', db='test',host='90b514053e09c9c7.c.cloudtogo.cn',port=38008)


class Index:
    def GET(self):
        return "Hello, world!GGG"
        
class Hello:
    def GET(self):
        msg = '''
        <h1>Web.py</h1>
        Hello,web.py!<br><br>
        I am Victor!<br>
        ABCDEFGH
        '''
        return msg

class Aname:
    def GET(self,name):
        return render.name(name)

class Data:
    def GET(self):
        d = db.select('app1_test')
        return render.data(d)

class Add:
    def POST(self):
        i = web.input()
        n = db.insert('app1_test',name=i.nn)
        raise web.seeother('/data')