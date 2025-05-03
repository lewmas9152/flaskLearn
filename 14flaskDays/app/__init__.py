from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>I am Samwel Njuguna and i am exicited to start this 14days learning challange</h1>"

@app.route("/about")
def about():
    return "<p>Hey, i  am a giy you can't exhaust info about in one sitting, why do't we grab  cup of tea and i will tell you all about sam</p>"


@app.route("/intro/<name>")
def intro(name):
    return render_template("base.html", name = name)