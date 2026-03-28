from flask import Blueprint, request, jsonify

voice_bp = Blueprint("voice", __name__)

@voice_bp.route("/voice", methods=["POST"])
def handle_voice():
    data = request.json

    user_input = data.get("text", "")

    # Temporary response
    return jsonify({
        "message": "Received input",
        "input": user_input
    })