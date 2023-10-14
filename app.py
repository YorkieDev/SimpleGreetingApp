from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "BigDirtyStinking_Bass666"

@app.route("/hello")
def index():
    flash("What is Your Name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hey " + str(request.form['name_input']) + ", it's so nice to meet you! ")
    return render_template("index.html")
