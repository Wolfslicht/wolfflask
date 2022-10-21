from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<path:path>")
def works(path):
    return render_template(path)