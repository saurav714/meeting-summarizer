import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [transcript, setTranscript] = useState('');
  const [summary, setSummary] = useState('');
  const [model, setModel] = useState('hf');

  const handleFileUpload = (e) => setFile(e.target.files[0]);

  const handleTranscribe = async () => {
    const formData = new FormData();
    formData.append('file', file);
    const res = await axios.post('http://localhost:5000/transcribe', formData);
    setTranscript(res.data.transcript);
  };

  const handleSummarize = async () => {
    const res = await axios.post('http://localhost:5000/summarize', {
      text: transcript,
      model,
    });
    setSummary(res.data.summary);
  };

  return (
    <div className="p-8 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">AI-Powered Meeting Summarizer</h1>
      <input type="file" onChange={handleFileUpload} className="mb-4" />
      <button onClick={handleTranscribe} className="bg-blue-500 text-white px-4 py-2 rounded mr-2">Transcribe</button>
      <select onChange={(e) => setModel(e.target.value)} className="px-2 py-1 border rounded mr-2">
        <option value="hf">Hugging Face (Pegasus)</option>
        <option value="ollama">Ollama (Mistral)</option>
      </select>
      <button onClick={handleSummarize} className="bg-green-600 text-white px-4 py-2 rounded">Summarize</button>

      {transcript && (
        <div className="mt-6">
          <h2 className="text-xl font-semibold">Transcript</h2>
          <textarea value={transcript} readOnly className="w-full h-40 border p-2 mt-2" />
        </div>
      )}

      {summary && (
        <div className="mt-6">
          <h2 className="text-xl font-semibold">Summary</h2>
          <textarea value={summary} readOnly className="w-full h-40 border p-2 mt-2" />
        </div>
      )}
    </div>
  );
}

export default App;
