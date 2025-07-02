import streamlit as st
from transcribe import transcribe_audio
from summarize import generate_summary

st.title("📝 Meeting Summarizer")
uploaded = st.file_uploader("Upload your meeting audio", type=["mp3", "wav"])

if uploaded:
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded.read())
    st.text("🔁 Transcribing...")
    transcript = transcribe_audio("temp_audio.mp3")
    st.text_area("Transcript", transcript, height=200)

    if st.button("Generate Summary"):
        st.text("✂️ Summarizing...")
        summary = generate_summary(transcript)
        st.success("✅ Summary:")
        st.text_area("Summary", summary, height=200)
