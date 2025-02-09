from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API Key (replace with your actual key)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Generate AI response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
