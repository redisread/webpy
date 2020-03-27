import web

# 定义网页的所有地址
urls = (
    '/','index'
)

# 新建网页App
app = web.application(urls,globals()) # globals() 函数会以字典类型返回当前位置的全部全局变量。

if __name__ == "__main__":
    pass
