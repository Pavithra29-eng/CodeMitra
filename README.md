# 🚀 CodeMitra

CodeMitra is a multilingual programming error explanation app that helps
beginner programmers — especially learners more comfortable with Hindi or
Marathi than English — understand Python errors in their own language.

Instead of just showing `NameError: name 'x' is not defined`, CodeMitra explains:
- **What happened?**
- **Why did it happen?**
- **How do I fix it?**

...in **English, Hindi, or Marathi**.

## Features (v1)

- Paste Python code and run it directly in the app
- Automatic error detection (type + message)
- Beginner-friendly explanations from a curated knowledge base
- Supports 10 common beginner errors: `SyntaxError`, `NameError`, `TypeError`,
  `ValueError`, `IndexError`, `KeyError`, `ZeroDivisionError`,
  `IndentationError`, `AttributeError`, `FileNotFoundError`
- Code runs in an isolated subprocess with a timeout, not in the app's own process

## Project structure

```
codemitra/
├── app.py              # Streamlit UI
├── runner.py           # Safely executes user code in a subprocess
├── knowledge_base.py   # Error explanations in English/Hindi/Marathi
├── requirements.txt
└── README.md
```

## Run locally

```bash
git clone https://github.com/<your-username>/codemitra.git
cd codemitra
python3 -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`).

## Deploy for free (Streamlit Community Cloud)

1. Push this project to a **public** GitHub repository (see below).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"New app"**, choose your repo, branch (`main`), and set the main
   file path to `app.py`.
4. Click **Deploy**. Your app will get a public URL like
   `https://codemitra-<random>.streamlit.app`.

## Push this project to GitHub

From inside the `codemitra` folder:

```bash
git init
git add .
git commit -m "Initial commit: CodeMitra MVP"
git branch -M main
git remote add origin https://github.com/<your-username>/codemitra.git
git push -u origin main
```

(Create the empty repo first on github.com, without a README, so there's no
merge conflict.)

## Roadmap

- [ ] AI/LLM layer (Ollama local model) for errors not in the knowledge base
- [ ] Code explanation mode ("what does this loop do?")
- [ ] Error history tracking per session
- [ ] Voice explanations (text-to-speech in Hindi/Marathi)
- [ ] Support for more languages
- [ ] Support for more programming languages (C++, Java, JavaScript)

## License

MIT — feel free to use and extend.
