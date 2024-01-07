from threading import Thread

from flask import Flask

app = Flask('')


@app.route('/')
def home():
    return ("halo, bot hidup")


def run():
    app.run(host="0.0.0.0", port=8081)


def alive():
    t = Thread(target=run)
    t.start()
