from transformers import pipeline

summarizer = pipeline("summarization", model="google/pegasus-xsum")

def generate_summary(text):
    chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
    summary = ""
    for chunk in chunks:
        out = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
        summary += out[0]['summary_text'] + " "
    return summary
