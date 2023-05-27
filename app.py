import openai
import gradio as gr
import asyncio

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, api_key=openai.api_key
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

async def main():
    iface = gr.Interface(fn=chatbot, inputs="textbox", outputs="textbox", title="AI Chatbot",
                         description="Ask anything you want", theme="compact")
    iface.launch()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
