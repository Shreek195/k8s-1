from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Flask App - Version 2.0 UPDATED successfully!</h1>"


if __name__ == "__main__":
    # Running on port 6000 as required
    app.run(host="0.0.0.0", port=6000)
