from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "your-openai-api-key"  # Replace with your actual API key

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"response": "Please enter a message!"})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
