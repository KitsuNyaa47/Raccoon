from multiprocessing.util import debug

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/form")

def form():
    return render_template("form.html")

@app.route("/submit", methods = ["POST"])

def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    return render_template("submit.html", name = name, email = email)

if __name__ == "__main__":
    app.run(debug=True)