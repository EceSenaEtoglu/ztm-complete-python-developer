from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<username>/<int:id>") # if we don't specify the variable type, it will be taken as string by default.
def blog_post(username = None,id = None):
    return render_template('userblog.html',name = username,b_id = id)

# by default 'render_template' looks in the 'templates' folder in the same directory for the given file.
# and the '.html' file might be pointing to '.css' and '.js' file,
# but 'render_template' will only allow those files if they are in 'static' folder.
@app.route("<username>")
def hello_world(username = None):
    return render_template("index.html",name = username)


@app.route("/about")
def blogs():
    return render_template("about.html")

