from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/connect.html")
def connect():
    return render_template("connect.html")

@app.route("/profile.html")
def profile():
    return render_template("profile.html")


if __name__=="__main__":
    app.run()