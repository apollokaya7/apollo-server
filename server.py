from flask import Flask, request, jsonify

app = Flask(__name__)

# einfache Datenbank im Speicher
licenses = {
    "APOLLO-1234": None
}

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    key = data["key"]
    hwid = data["hwid"]

    if key not in licenses:
        return jsonify({"valid": False})

    # erste Aktivierung
    if licenses[key] is None:
        licenses[key] = hwid
        return jsonify({"valid": True, "msg": "Activated"})

    # HWID check
    if licenses[key] == hwid:
        return jsonify({"valid": True, "msg": "OK"})

    return jsonify({"valid": False, "msg": "HWID blocked"})


app.run(port=5000)