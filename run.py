from app import create_app
import os

app = create_app()
print(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

if __name__ == "__main__":
    app.run(debug=True)