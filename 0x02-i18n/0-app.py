#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """GET /
    """
    return render_template('0-index.html')
