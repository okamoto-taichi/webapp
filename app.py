from flask import Flask, request, render_template, jsonify
#from flask_sqlalchemy import SQLAlchemy
#from test_model import Person
app = Flask(__name__)

@app.route('/try_html')
def try_html():
    return render_template('try_html.html')
