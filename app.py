from flask import Flask

app = Flask(__name__)

@app.route("/homepage")
def home_page():
	return "Welcome to chuckedudodu's home page!"

@app.route("/")
def hello_world():
	return "Welcome to chuckedudodu Service!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
