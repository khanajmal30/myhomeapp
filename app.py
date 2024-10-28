from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_ENDPOINT = 'https://api.example.com/ai-endpoint'  # Replace with your AI API endpoint
API_KEY = 'your_api_key'  # Replace with your AI API key

@app.route('/api/ai-response', methods=['POST'])
def get_ai_response():
    user_input = request.json.get('input')
    response = requests.post(API_ENDPOINT, headers={'Authorization': f'Bearer {API_KEY}'}, json={'input': user_input})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
