from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Flask App - Version 1.0 running on Port 6000</h1>"


if __name__ == "__main__":
    # Running on port 6000 as required
    app.run(host="0.0.0.0", port=6000)
