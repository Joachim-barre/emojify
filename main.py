from utils import emojify
from flask import Flask, render_template

app = Flask(__name__, template_folder="html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<text>") 
def emojifier(text): 
    return render_template("emojifier.html", result=emojify(text))

if __name__ == "__main__":
    app.run()
