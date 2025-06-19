import gradio as gr

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.summarizer import generate_summary

def summarize_input(text):
    return generate_summary(text)

demo=gr.Interface(
    fn=summarize_input,
    inputs=gr.Textbox(lines=10, label="Enter text to summarize"),
    outputs=gr.Textbox(label="Summary"),
    title="GenAssist",
    description="LLM-powered summarizer using BART"
)

if __name__=="__main__":
    demo.launch()


