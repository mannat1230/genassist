import gradio as gr
from app.summarizer import generate_summmary

def summarize_input(text):
    return generate_summary(text)

demo=gr.interface(
    fn=summarize_input,
    inputs=gr.Textbox(lines=10, label="Enter text to summarize"),
    outputs=gr.Textbox(label="Summary"),
    title="GenAssist",
    description="LLM-powered summarizer using BART"
)

if __name__=="__main__":
    demo.launch()