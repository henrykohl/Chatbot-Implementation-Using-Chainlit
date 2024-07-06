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

