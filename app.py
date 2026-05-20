from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:
        user_message = request.json["message"]

        prompt = f"""
        You are an AI marketing assistant for small businesses.

        Help users with:
        - Instagram captions
        - Promotional offers
        - Marketing ideas
        - Customer engagement ideas

        User request:
        {user_message}
        """

        response = model.generate_content(prompt)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:

        return jsonify({
            "reply": f"Error: {str(e)}"
        })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)