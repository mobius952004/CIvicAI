import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_key")
    PROJECT_ID = os.getenv("PROJECT_ID")
    REGION = os.getenv("REGION")
    MODEL_NAME = os.getenv("MODEL_NAME")

    # Future integrations
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")