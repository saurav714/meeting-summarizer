# 📁 backend/summarize.py

import os
import requests
from transformers import pipeline

# Load Hugging Face summarizer only once
def summarize_with_huggingface(text):
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    summarizer = pipeline("summarization", model="google/pegasus-xsum", token=hf_token)
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
    return summary

def summarize_with_ollama(text):
    payload = {
        "model": os.getenv("OLLAMA_MODEL", "mistral"),
        "prompt": f"Summarize the following meeting transcript:\n{text}"
    }
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    response.raise_for_status()
    return response.json().get("response", "[Ollama failed to return a summary]")
