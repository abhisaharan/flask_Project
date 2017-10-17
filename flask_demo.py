from flask import Flask, render_template

app = Flask(__name__)   #new instance of the class flask


@app.route('/')     #map the url the python function index.
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
