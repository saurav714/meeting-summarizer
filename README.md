# 📝 Meeting Summarizer

A local + Colab-ready app that transcribes meeting audio and generates concise summaries using Whisper + a transformer LLM.

## 🔧 Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run app.py
```

## 🚀 Colab

A `colab_meeting_summarizer.ipynb` is included for cloud use with Google Drive audio files.

## 📁 Structure

- `app.py` - Streamlit app
- `transcribe.py` - Whisper-based transcription
- `summarize.py` - LLM-based summarization
- `data/sample.mp3` - Example meeting audio
