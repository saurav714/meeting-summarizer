from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_id = "google/pegasus-xsum"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def generate_summary(text):
    chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
    summary = ""
    for chunk in chunks:
        out = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
        summary += out[0]['summary_text'] + " "
    return summary
