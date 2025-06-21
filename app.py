from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

STABILITY_API_KEY = "sk-yeCWQamWQ3iNgdVzIciE9AlgwsXDDx4aA1aDsquQ5nF892SL"
STABILITY_API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "output_format": "png"
    }

    response = requests.post(STABILITY_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get("image")  # Adjust based on API response
    else:
        return None

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    image_url = generate_image(user_input)
    if image_url:
        return jsonify({"response": f"Here is your image: {image_url}"})
    else:
        return jsonify({"error": "Failed to generate image"}), 500

if __name__ == "__main__":
    app.run(debug=True)
