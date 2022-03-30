from flaskr import app
from flask import render_template

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/531program')
def program531():
    return render_template(
        '531program.html'
    )