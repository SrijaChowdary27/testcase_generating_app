# run.py
from app.routes.app import app  # import the Flask app instance

if __name__ == "__main__":
    print("Starting Flask backend on http://127.0.0.1:5000")
    app.run(debug=True)
