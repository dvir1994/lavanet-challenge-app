# Entrypoint of the Flask application
from app import app
import logging
if __name__ == "__main__":
    app.run()
