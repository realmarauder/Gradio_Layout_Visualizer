"""Minimal test app for automated testing"""

import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# Test App")

if __name__ == "__main__":
    demo.launch()
