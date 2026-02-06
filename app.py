from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", day_count=30)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
