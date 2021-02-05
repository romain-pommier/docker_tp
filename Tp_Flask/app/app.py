import sys, os
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#route for home page

@app.route("/")
def index():
    return "<h1> hello BG </h1>"

@app.route("/mon_nom/")
def myName():
    return "<h1> hello Mon nom </h1>"

@app.route("/mon_nom/<name>")
def MyCustomName(name):
    return 'Mon nom est {}'.format(escape(name))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)


