from flask import Flask, render_template

view = Flask(__name__)

@view.route('/')
def home():
    return render_template("home.html")

@view.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    view.run(debug=True)
    