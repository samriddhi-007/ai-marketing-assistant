from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json["message"]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            You are an AI marketing assistant for small businesses.

            User request:
            {user_message}
            """
        )

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": str(e)
        })
    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)