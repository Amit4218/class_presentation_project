from flask import Flask, jsonify
from db import get_random_riddle

app = Flask(__name__)


@app.route("/get-random-riddle")
def random_riddle():
    riddle = get_random_riddle()
    return jsonify(riddle) 


if __name__ == "__main__":
    app.run(debug=True)
