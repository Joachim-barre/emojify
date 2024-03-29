from utils import emojify, demojify
import argparse
from flask import Flask, render_template, redirect, url_for, request 

app = Flask(__name__, template_folder="html")
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encoder(): 
    if request.method == 'POST':
        text = request.form['to_encode']
        return emojify(text)
    return redirect(url_for('home'))

@app.route("/decode", methods=["POST"])
def decoder(): 
    if request.method == 'POST':
        text = request.form['to_decode']
        return demojify(text)
    return redirect(url_for('home'))


def main():
    parser = argparse.ArgumentParser(
                    prog='Emojify',
                    description='Web app that encode text to emoji')
    parser.add_argument('-d', '--debug',
                    action='store_true')
    parser.add_argument('-a', '--address',
                    help="address that the app should use",
                    default="127.0.0.1")
    args = parser.parse_args()
    app.run(debug=args.debug,host=args.address)

if __name__ == "__main__":
    main()
