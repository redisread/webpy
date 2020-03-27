import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        msg = '''
        <h1>Web.py</h1>
        Hello,web.py!<br><br>
        I am Victor!<br>
        '''
        return msg

if __name__ == "__main__":
    app.run()