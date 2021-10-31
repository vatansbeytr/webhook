from flask import Flask

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
	return request.form['hub_challenge']

if __name__ == '__main__':
    app.run(debug=True)
