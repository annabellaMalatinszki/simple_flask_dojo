from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/request-counter", methods=["GET", "POST"])
def request_counter():
    return render_template("simple_flask_dojo.html")


@app.route("/statistics", methods=["GET"])
def statistics():
    return "Statistics"


if __name__ == "__main__":
    app.run(debug=True)
