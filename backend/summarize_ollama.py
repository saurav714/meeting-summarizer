import requests

def summarize_with_ollama(text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": f"Summarize the following meeting transcript:\n\n{text}",
            "stream": False
        }
    )
    return response.json().get("response", "[Error] No summary returned.")
