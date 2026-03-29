from flask import Blueprint, request, jsonify
from app.services.orchestrator import extract_user_info
from app.services.rag_engine import fetch_relevant_schemes
from app.services.llm_services import generate_response

voice_bp = Blueprint("voice", __name__)

@voice_bp.route("/voice", methods=["POST"])
def handle_voice():
    data = request.json

    text = data.get("text", "")

    user_profile = extract_user_info(text)
    schemes = fetch_relevant_schemes(user_profile)
    final_response = generate_response(text, schemes)

    return jsonify(
        {
            "input":text,
            "extracted":user_profile,
            "schemes":schemes,
            "Response":final_response
        }
    )