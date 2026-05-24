import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Apollo Server Online"

@app.route("/check", methods=["POST"])
def check():
    return jsonify({"valid": True})

# WICHTIG: Render Port ZWINGEND korrekt binden
if __name__ == "__main__":
    port = int(os.environ.get("PORT"))
    app.run(host="0.0.0.0", port=port)
