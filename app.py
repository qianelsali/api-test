from flask import Flask, request, Response, render_template, jsonify

app = Flask(__name__)

@app.route("/homepage")
def home_page():
	return "Welcome to wokedudodo's home page!"

@app.route("/")
def hello_world():
	return "Welcome to wokedudodo Service!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
