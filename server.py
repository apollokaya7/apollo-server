from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Apollo Server Online"

@app.route("/check", methods=["POST"])
def check():
    return jsonify({"valid": True})
