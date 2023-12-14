from utils import emojify
from flask import Flask, render_template, redirect, url_for, request 

app = Flask(__name__, template_folder="html")
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encoder(): 
    if request.method == 'POST':
        return emojify(text)
    return redirect(url_for('home'))

if __name__ == "__main__":

    app.run()
