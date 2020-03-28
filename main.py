import web
import test
from todo_app import todo
from blog_app import blog
# # 指定模板目录
# render = web.template.render('templates')
# # 连接数据库
# db = web.database(dbn='mysql', user='root', pw='123456', db='test',host='90b514053e09c9c7.c.cloudtogo.cn',port=38008)

# 定义网页的所有地址
urls = (
    '/','Index',
    '/test',test.app_test,
    '/todo',todo.app_todo,
    '/blog',blog.app_blog
)   

render = web.template.render("templates")

# 网页访问的处理类
class Index:
    def GET(self):
        return render.index()
        

if __name__ == "__main__":  
    # 新建网页App
    app = web.application(urls,locals()) # globals() 函数会以字典类型返回当前位置的全部全局变量
    # 运行程序
    app.run()
