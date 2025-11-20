"""Example: Simple Chatbot Interface

This example demonstrates how to use the enhanced visual builder
to create a chatbot interface.
"""

import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# My Chatbot")
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(label="Your message", placeholder="Type here...")
    submit = gr.Button("Send")

    @submit.click(inputs=[msg], outputs=[chatbot])
    def respond(message):
        return [[message, "This is a response"]]

demo.launch(inbrowser=True)  # Auto-open browser
