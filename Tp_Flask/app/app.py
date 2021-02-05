import sys, os
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

#route for home page

@app.route("/")
def index():
    return "<h1> hello BG </h1>"

@app.route("/mon_nom/<name>")
def MyCustomName(name):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)


