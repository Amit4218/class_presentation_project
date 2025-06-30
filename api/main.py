from flask import Flask, render_template
from db import get_random_riddle

app = Flask(__name__)


@app.route("/get-random-riddle")
def random_riddle():
    riddle = get_random_riddle()
    return render_template("riddle.html", questions=riddle)


@app.route("/")
def index():
    return render_template("index.html")    


if __name__ == "__main__":
    app.run(debug=True)
