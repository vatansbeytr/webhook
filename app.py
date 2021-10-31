from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
	print(str(request.get_data()))
	return request.args.get('hub.challenge')

@app.route('/page')
def page():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
