import chainlit as cl
from src.llm import ask_order, messages

## 第一次要開始執行 async def main 時, messages 是 llm.py 中的 messages 內容
## 每執行一次 async def main 後, messages 會多包含一個 我們最新的輸入內容 以及 最新的response

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    messages.append({"role": "user", "content": message.content}) ## message.content 是 我們輸入的內容
    response = ask_order(messages)
    messages.append({"role": "assistant", "content": response})

    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()

