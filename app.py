from flask import Flask, request, Response, render_template, jsonify

app = Flask(__name__)

@app.route("/homepage")
def hello_world():
	return "Welcome to my Service!"


