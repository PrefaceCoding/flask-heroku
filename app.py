from flask import Flask, render_template
import datetime

app = Flask(__name__)


# index page
@app.route("/")
def index():
    return "Hello Dazi"


@app.route("/Ehsan")
def ehsan():
    return "Hello Ehsan"

@app.route("/<string:name>")
def name(name):
    name = name.capitalize()
    return render_template("hello.html", name = name)

@app.route("/is<string:day>")
def sat(day):
    day = day.capitalize()
    now = datetime.datetime.now()

    if now.strftime("%A") == day:
        return "yes"
    else:
        return "no"

@app.route("/friday")
def fri():
    now = datetime.datetime.now()
    weekday = now.weekday()

    return render_template("friday.html", weekday = weekday)

@app.route("/hellov2")
def hellov2():
    return render_template("hello.html")

@app.route("/up")
def up():
    return render_template("up.html")
