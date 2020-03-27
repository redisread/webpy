import web
# 指定模板目录
render = web.template.render('templates')
# 连接数据库
db = web.database(dbn='mysql', user='root', pw='123456', db='test',host='90b514053e09c9c7.c.cloudtogo.cn',port=38008)
# 定义网页的所有地址
urls = (
    '/','index',
    '/temp','temp',
    '/name/(.*)','Aname',
    '/base','Mybase',
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

class Mybase:
    def GET(self):
        return render.base("3.1415926")

class Data:
    def GET(self):
        d = db.select('app1_test')
        return render.data(d)

class Add:
    def POST(self):
        i = web.input()
        n = db.insert('app1_test',name=i.nn)
        raise web.seeother('/data')

if __name__ == "__main__":  
    # 新建网页App
    app = web.application(urls,globals()) # globals() 函数会以字典类型返回当前位置的全部全局变量
    # 运行程序
    app.run()
