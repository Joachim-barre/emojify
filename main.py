from utils import emojify
from flask import Flask, render_template, redirect, url_for 

app = Flask(__name__, template_folder="html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encoder(): 
    pass

if __name__ == "__main__":

    app.run()
