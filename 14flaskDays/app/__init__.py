from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello</p>"

@app.route("/form", methods= ["POST", "GET"])
def form():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        data = {
            "name": name,
            "email":email
        }
        return data

    return render_template('base.html') 
        

