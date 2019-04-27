from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('header.html')
    #return 'Hello there, welcome to our app!'


@app.route('/map')
def map_page():
    return render_template('map.html')
