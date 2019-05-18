#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api")
def api():
    return jsonify({'key': 'value'})


if __name__ == "__main__":
    app.run()