from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect("https://registry.jsonresume.org/jeremy-hicks")
