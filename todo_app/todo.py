""" Basic todo list using webpy 0.3 """
import web
import todo_app.model as model

### Url mappings

urls = (
    "/", "Index",
    "/del/(\d+)", "Delete",
    '/hello','Hello'
    )


### Templates 默认从根目录开始寻找
render = web.template.render("todo_app/templates/",base="base")

class Hello:
    def GET(self):
        return render.test()

class Index:

    form = web.form.Form(
        web.form.Textbox("title", web.form.notnull, description="I need to:"),
        web.form.Button("Add todo"),
    )

    def GET(self):
        """ Show page """
        todos = model.get_todos()
        form = self.form()
        return render.index(todos, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother("/")


class Delete:
    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother("/")

app_todo = web.application(urls, locals())