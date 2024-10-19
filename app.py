import os
import gradio as gr
import requests

os.environ["HUGGINGFACE_TOKEN"] = "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"

def cevir(text):
    basliklar = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}
    yanit = requests.post("https://api-inference.huggingface.co/models/google-t5/t5-base",
                             basliklar=basliklar, json={"inputs": text})
    return yanit.json()

iface = gr.Interface(fn=cevir, inputs="text", outputs="json")
iface.launch(share=True)
