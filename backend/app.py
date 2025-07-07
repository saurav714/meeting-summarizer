# 📁 backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from summarize import summarize_with_huggingface, summarize_with_ollama

app = Flask(__name__)
CORS(app)
load_dotenv()

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")
    model = data.get("model", "huggingface")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    if model == "ollama":
        summary = summarize_with_ollama(text)
    else:
        summary = summarize_with_huggingface(text)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)