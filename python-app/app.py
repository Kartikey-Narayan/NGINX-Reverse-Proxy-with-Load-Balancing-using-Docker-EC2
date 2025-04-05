# Import necessary modules from Flask
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Home 
@app.route('/')
def home():
    return jsonify({
        "status": "✅ OK",
        "message": "🐍 Hello from Python Flask App!"
    }), 200

# Health 
@app.route('/health')
def health():
    return jsonify({
        "status": "✅ OK",
        "message": "💚 Healthy and running smoothly! - From Python Flask App"
    }), 200

# Catch all undefined routes with a 404 response
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error": "❌ Not Found",
        "message": "⚠️ The requested route does not exist - From Python Flask App."
    }), 404

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)