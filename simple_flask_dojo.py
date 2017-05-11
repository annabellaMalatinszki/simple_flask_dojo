from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

counter_dict = {"GET": 0, "POST": 0, "DELETE": 0, "PUT": 0}


@app.route("/")
def home_page():
    return render_template("simple_flask_dojo.html", counter_dict=counter_dict)


@app.route("/request-counter", methods=["GET", "POST", "DELETE", "PUT"])
def request_counter():
    global counter_dict
    if request.method == "GET":
        counter_dict["GET"] += 1
    if request.method == "POST":
        counter_dict["POST"] += 1
    if request.method == "DELETE":
        counter_dict["DELETE"] += 1
    if request.method == "PUT":
        counter_dict["PUT"] += 1
    return redirect(url_for('home_page'))


@app.route("/statistics", methods=["GET"])
def statistics():
    return "Statistics"


if __name__ == "__main__":
    app.run(debug=True)
