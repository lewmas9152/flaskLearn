from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods= ["POST", "GET"])
def form():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get("Password")
        data = {
            "name": name,
            "email":email,
            "password":password
        }
        return data

    return render_template('base.html') 
        

