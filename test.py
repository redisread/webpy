import web
# 指定模板目录
render = web.template.render('templates')
# 连接数据库
db = web.database(dbn='mysql', user='root', pw='123456', db='test',host='90b514053e09c9c7.c.cloudtogo.cn',port=38008)
# 定义网页的所有地址
urls = (
    '/','index',
    '/index','index',
    '/temp','temp',
    '/name/(.*)','Aname',
    '/data','Data',
    '/add','Add'
)   

# 网页访问的处理类
class index:
    def GET(self):
        return "Hello, world!GGG"

class temp:
    def GET(self):
        return render.temp()

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

# 定义局部应用
app_test = web.application(urls,locals())

