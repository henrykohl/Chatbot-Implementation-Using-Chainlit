# Chatbot-Implementation-using-Chainlit 
[Official Webise](https://docs.chainlit.io/get-started/overview)


## How to run?

1. Create a virtual environment

```bash
conda create -n llmapp python=3.10 -y
# or
virtualenv llmapp --python=python3.10 # virtualenv llmapp -p python3.10
```

2. Activate the environment

```bash
conda activate llmapp
# or
source ./llmapp/bin/activate
```

* 建立 `requirements.txt`
> ```
> chainlit
> ```

3. Install the required packages

```bash
pip install -r requirements.txt
```


## chainlit commands

```bash
chainlit init
```
* 建立 `app.py`

```bash
chainlit run app.py
```

## 補充--用 commands 完成 github 更新
```bash
git add .

git commit -m "updated"

git push origin main
```
---
# Day 2

`.chainlit/config.toml` 中

```python
[UI]
# Name of the assistant.
name = "Assistant"
```
`Assistant` 可以修改 `Zomato Chatbot`

* 建立 `.env` 檔案
```
OPENAI_API_KEY="..."
```

* 建立 `src` 資料夾
> `__init__.py`
>
> `llm.py`
>
> `prompt.py`

* 建立 `setup.py` 檔案

* 修改 `requirements.txt`
> ```
> chainlit
> openai
> python-dotenv
> -e .
> ```

重新安裝 必要的 packages
```bash
pip install -r requirements.txt
```

* 修改 `chainlit.md` （原內容如下）
```markdown
# Welcome to Chainlit! 🚀🤖

Hi there, Developer! 👋 We're excited to have you on board. Chainlit is a powerful tool designed to help you prototype, debug and share applications built on top of LLMs.

## Useful Links 🔗

- **Documentation:** Get started with our comprehensive [Chainlit Documentation](https://docs.chainlit.io) 📚
- **Discord Community:** Join our friendly [Chainlit Discord](https://discord.gg/k73SQ3FyUh) to ask questions, share your projects, and connect with other developers! 💬

We can't wait to see what you create with Chainlit! Happy coding! 💻😊

## Welcome screen

To modify the welcome screen, edit the `chainlit.md` file at the root of your project. If you do not want a welcome screen, just leave this file empty.
```

* 修改 `app.py` (原內容如下)
```python
import chainlit as cl


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()
```    
