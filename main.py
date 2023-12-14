from utils import emojify
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

def main():
    parser = argparse.ArgumentParser(
                    prog='Emojify',
                    description='Web app that encode text to emoji')
    parser.add_argument('-d', '--debug',
                    action='store_true')
    args = parser.parse_args()
    app.run(debug=args.debug)

if __name__ == "__main__":
    main()
