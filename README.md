# 🧠 AI-Powered Meeting Summarizer

A full-stack application that transcribes, diarizes, and summarizes meeting audio using local and cloud-based AI models. Supports Whisper, Pegasus, and Ollama with an optional Colab notebook for heavy tasks.

---

## 📦 Project Structure

```
meeting-summarizer/
├── backend/
│   ├── app.py                 # Flask server
│   ├── transcribe.py          # Whisper transcription
│   ├── summarize.py           # Pegasus summarization
│   ├── summarize_ollama.py    # Ollama integration
│   └── diarize.py             # Placeholder for diarization
├── frontend/
│   ├── src/
│   │   └── App.jsx            # React frontend
│   └── package.json
└── AI_Meeting_Summarizer_Colab.ipynb  # Optional Colab notebook
```

---

## ⚙️ Setup Instructions

### 🔁 Backend (Flask)

```bash
cd backend
pip install flask flask-cors transformers torch torchaudio openai-whisper
python app.py
```

Runs on: `http://localhost:5000`

### 🧑‍💻 Frontend (React)

```bash
cd frontend
npm install
npm start
```

Opens at: `http://localhost:3000`

---

## 🧠 Features

- 🎙️ Upload audio (WAV/MP3)
- 🔊 Transcription using Whisper
- 👥 (Planned) Diarization using pyannote
- ✂️ Summarization using:
  - Pegasus (Hugging Face)
  - Ollama (Mistral) via local API
- 🧠 Optional Colab for large models

---

## ☁️ Google Colab Integration

> Use this when your system can't handle Whisper Large or diarization locally.

1. Open `AI_Meeting_Summarizer_Colab.ipynb` in [Google Colab](https://colab.research.google.com/)
2. Upload audio
3. Get:
   - `transcript.txt`
   - `diarization.txt`
   - `summary.txt`

---

## 🛠️ Configuration

### 📍 Ollama

Ensure Ollama is running locally and has a supported model pulled:

```bash
ollama run mistral
```

### 🧪 Hugging Face

No token needed for Pegasus, but diarization in Colab requires:

- [Create token](https://huggingface.co/settings/tokens)
- Paste it into the Colab variable `HUGGINGFACE_TOKEN`

---

## 🚀 Roadmap

- [x] Whisper-based transcription
- [x] Pegasus and Ollama summarization
- [ ] Diarization in Flask (via pyannote)
- [x] Colab GPU support for large models
- [ ] Auto-upload via file.io (optional)

---

## 🤝 Credits

Built with:
- OpenAI Whisper
- Hugging Face Transformers
- Ollama
- Pyannote Audio
- React + Flask

---


