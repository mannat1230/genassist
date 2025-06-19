from transformers import pipeline

# Load summarization pipeline once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, max_length=130, min_length=30):
    if not text.strip():
        return "Input text is empty."
    result = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return result[0]['summary_text']