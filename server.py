import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Apollo Server Online"

@app.route("/check", methods=["POST"])
def check():
    return jsonify({"valid": True})

port = int(os.environ.get("PORT", 10000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

