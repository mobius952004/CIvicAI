import vertexai
from vertexai.generative_models import GenerativeModel
from flask import current_app


def init_model():
    vertexai.init(
        project=current_app.config["PROJECT_ID"],
        location=current_app.config["REGION"]
    )
    return GenerativeModel(current_app.config["MODEL_NAME"])


def generate_response(user_query, schemes):
    model = init_model()

    # Build context
    scheme_text = ""
    for s in schemes:
        scheme_text += f"""
        Scheme: {s['name']}
        Eligibility: {s['eligibility']}
        Documents: {', '.join(s['documents'])}
        """

    prompt = f"""
    You are a helpful government assistant.

    User Query:
    {user_query}

    Relevant Schemes:
    {scheme_text}

    Instructions:
    - Answer in simple Hindi
    - Explain clearly which schemes apply
    - Mention eligibility and documents
    - Keep it conversational and easy
    """

    response = model.generate_content(prompt)

    return response.text