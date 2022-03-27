
from flask import Flask, render_template, request
from ml_model import make_prediction

app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/sub",methods=["POST"])
def submit():
    # HTML -> .py
    if request.method=="POST":
        age=request.form["age"]
        salary=request.form["salary"]
        if make_prediction(age,salary):
            return render_template("sub.html",a="You can get credit")
    return render_template("sub.html",a="You can not get credit")

if __name__=="__main__":
    app.run()