#!/usr/bin/python3
# A flask web service app that displays hello world as plain text

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
