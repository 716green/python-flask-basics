#!python3

from flask import Flask, request, render_template
app = Flask(__name__)
app.config['DEBUG'] = True # auto refresh like nodemon

# Decorator
@app.route('/', methods=['GET', 'POST'])
def rootpage():
  name = ''
  food = ''
  if request.method == 'POST' and 'username' in request.form:
    name = request.form.get('username')
    food = request.form.get('userfood')
  return render_template('index.html', name=name, food=food)

@app.route('/welcome')
def welcome():
  return "Hello World from Flask app"

@app.route('/method', methods=['GET', 'POST'])
def method():
  if request.method == 'POST':
    return "POST request"
  else:
    return "GET request"



app.run()