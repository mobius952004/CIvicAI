from flask import Blueprint, request, jsonify
from app.services.orchestrator import extract_user_info

voice_bp = Blueprint("voice", __name__)

@voice_bp.route("/voice", methods=["POST"])
def handle_voice():
    data = request.json

    text = data.get("text", "")

    user_profile = extract_user_info(text)

    # Temporary response
    return jsonify(
        {
            "input":text,
            "extracted":user_profile
        }
    )