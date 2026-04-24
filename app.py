import os
import sys

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Import Flask app from backend
from main import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
