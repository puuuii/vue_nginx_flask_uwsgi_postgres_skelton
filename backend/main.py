#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


@app.route("/api")
def api():
    return jsonify({'key': 'value'})


if __name__ == "__main__":
    app.run()