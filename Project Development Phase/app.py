from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/registering")
def render_registering():
    return render_template("registering.html",message="")

@app.route("/signin")
def render_signin(accountok=True):
    if accountok== True:
        return render_template("signin.html",message="")
    else:
        return render_template("signin.html",message="Username / Password is Wrong")



@app.route("/login",methods = ['POST'])
def checkLogin():
    email = request.form['email']
    pwd = request.form['Password']
    if(email=="hello@abc.com" and pwd == "hello@123"):
        return render_template("home.html", user = "Everyone")
    else:
        return render_signin(False)

@app.route("/home")
def render_home():
    return render_template("home.html",message="")

@app.route("/dashboard")
def render_dashboard():
    return render_template("dashboard.html",message="")

@app.route("/expenses")
def render_expenses():
    return render_template("expenses.html",message="")
    

if __name__=="__main__":
    app.run(debug=True)