import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        msg = '''
        <h1>Web.py</h1>
        Hello,web.py!<br><br>
        I am Victor!<br>
<<<<<<< HEAD
        ABCDEFGH
=======
>>>>>>> 365186d691f8c3d237aa1e06b3853c597db86923
        '''
        return msg

if __name__ == "__main__":
    app.run()