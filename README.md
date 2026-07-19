# 💻 CodeMitra

CodeMitra is a web app that helps beginner programmers understand Python
errors in their own language — English, Hindi, or Marathi — instead of
confusing technical error messages.

## 🤔 The Problem

When beginners write code and hit an error like:
NameError: name 'x' is not defined

...it often makes no sense to someone new to programming. It's even harder
if English isn't their first language.

## ✅ What CodeMitra Does

1. You paste your Python code into the app.
2. CodeMitra runs it and detects the error (if any).
3. It explains the error in plain language, in **three parts**:
   - **What happened?**
   - **Why did it happen?**
   - **How do I fix it?**
4. You choose the explanation language: **English, Hindi, or Marathi**.

If the error is one of 10 common beginner errors, CodeMitra explains it
instantly using its own built-in knowledge base. If it's a rarer error,
CodeMitra asks an AI model to explain it on the spot — so no error goes
unexplained.

## 🎯 Try It

🔗 **Live demo:** [Paste your Streamlit link here]

Pick a sample error from the dropdown, or paste your own broken code, hit
**Run Code**, and see the explanation.

## 🛠️ How It Works (Under the Hood)
Your code
↓
Runs safely in an isolated process (so nothing crashes the app)
↓
Error caught?
├── No  → shows your program's output
└── Yes → looks up the error type
├── Known error (one of 10 common types) → local knowledge base
└── Unknown error → asks Groq's AI to explain it live
↓
Explanation shown in your chosen language

## 📦 Project Files

| File | What it does |
|---|---|
| `app.py` | The Streamlit web interface (what you see and click) |
| `runner.py` | Safely runs your code in a separate process and catches errors |
| `knowledge_base.py` | Beginner-friendly explanations for 10 common errors, in 3 languages |
| `ai_layer.py` | Calls Groq's free AI API to explain any error not in the knowledge base |
| `requirements.txt` | List of Python packages needed to run the app |

## ✨ Supported Errors (built-in, instant)

`SyntaxError`, `NameError`, `TypeError`, `ValueError`, `IndexError`,
`KeyError`, `ZeroDivisionError`, `IndentationError`, `AttributeError`,
`FileNotFoundError`

Any other error → explained live by AI.

## 🧰 Skills Used to Build This

- **Python** — all the core logic
- **Streamlit** — turns Python code into a web app with zero HTML/CSS/JS
- **`subprocess`, `tempfile`, `os`** (Python's standard library) — run user
  code safely in an isolated process instead of directly inside the app
- **Regex (`re`)** — reads Python's error messages and pulls out the error
  type and description
- **Generative AI / LLMs** — Groq's free API explains errors the knowledge
  base doesn't cover, in the user's chosen language (NLP + multilingual AI)
- **Git & GitHub** — version control and code hosting
- **Streamlit Community Cloud** — free public hosting, auto-deploys on every
  GitHub push
- **Localization** — hand-written Hindi and Marathi explanations for common
  errors

## 🚀 Run It Yourself

```bash
git clone https://github.com/Pavithra29-eng/CodeMitra.git
cd CodeMitra
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Get a free API key from [console.groq.com](https://console.groq.com), then
create a file `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your-key-here"
```

Run the app:

```bash
python -m streamlit run app.py
```

## 🌐 Deploy Your Own Copy (Free)

1. Push this project to your own public GitHub repo.
2. Go to [share.streamlit.io](https://share.streamlit.io) → sign in with GitHub.
3. Click **New app** → pick your repo → branch `main` → main file `app.py`.
4. Under **Settings → Secrets**, add your `GROQ_API_KEY`.
5. Click **Deploy**. You'll get a public link in a couple of minutes.

## 🗺️ What's Next

- [ ] Explain what a working code snippet does, not just errors
- [ ] Track error history in a session
- [ ] Read explanations aloud (text-to-speech) in Hindi/Marathi
- [ ] Support more languages
- [ ] Support more programming languages (C++, Java, JavaScript)

## 📄 License

MIT — free to use, modify, and share.
