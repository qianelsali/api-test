from flask import Flask, request, Response, render_template, jsonify

app = Flask(__name__)

@app.route("/homepage")
def hello_world():
	return "Welcome to my Service!"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
