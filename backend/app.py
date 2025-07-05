from flask import Flask, request, jsonify
from flask_cors import CORS
from transcribe import transcribe_audio
from summarize import generate_summary
from summarize_ollama import summarize_with_ollama
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HUGGINGFACE_TOKEN")
app = Flask(__name__)
CORS(app)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files['file']
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)
    transcript = transcribe_audio(audio_path)
    return jsonify({"transcript": transcript})

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get("text", "")
    model = data.get("model", "hf")
    if model == "hf":
        summary = generate_summary(text)
    elif model == "ollama":
        summary = summarize_with_ollama(text)
    else:
        summary = "[OpenAI fallback not implemented]"
    return jsonify({"summary": summary})

@app.route('/diarize', methods=['POST'])
def diarize():
    return jsonify({"message": "Diarization not implemented yet"})

if __name__ == '__main__':
    app.run(debug=True)
