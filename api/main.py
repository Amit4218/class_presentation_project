from flask import Flask, render_template, request
from db import get_random_riddle, create_session_token, submit_riddle, verify_answer

app = Flask(__name__)


@app.route("/get-random-riddle")
def random_riddle():
    riddle = get_random_riddle()
    token = create_session_token(riddle["_id"])
    return render_template("riddle.html", questions=riddle, token=token)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/verify-answer/<token>", methods=["POST"])
def handle_verify_answer(token):
    answer = request.form.get("answer")
    if not answer:
        return "<h1>No answer provided.</h1>"

    riddle = verify_answer(token, answer)
    return render_template("riddle.html", questions=riddle, token=token)


@app.route("/submit/<token>")
def submit_riddle_route(token):
    riddle = submit_riddle(token)
    return render_template("score.html", score=riddle)


@app.route("/get-random-riddle-cli")
def get_random_riddle_cli():
    riddle = get_random_riddle()
    return riddle


if __name__ == "__main__":
    app.run(debug=True)
