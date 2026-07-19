# 💻 CodeMitra

CodeMitra is a web app that helps beginner programmers understand Python errors in their own language — English, Hindi, or Marathi — instead of confusing technical error messages.

## 🤔 The Problem

When beginners write code and hit an error like:

```text
NameError: name 'x' is not defined

...it often makes no sense to someone new to programming. It's even harder if English isn't their first language.

✅ What CodeMitra Does
You paste your Python code into the app.
CodeMitra runs it and detects the error (if any).
It explains the error in plain language, in three parts:
What happened?
Why did it happen?
How do I fix it?
You choose the explanation language: English, Hindi, or Marathi.

If the error is one of 10 common beginner errors, CodeMitra explains it instantly using its own built-in knowledge base. If it's a rarer error, CodeMitra asks an AI model to explain it on the spot — so no error goes unexplained.

🎯 Try It

🔗 Live Demo: Open CodeMitra

Pick a sample error from the dropdown, or paste your own broken code, hit Run Code, and see the explanation.

🛠️ How It Works (Under the Hood)
Your code
    ↓
Runs safely in an isolated process
(so nothing crashes the app)
    ↓
Error caught?
    ├── No  → Shows your program's output
    │
    └── Yes → Looks up the error type
              │
              ├── Known error
              │   (one of 10 common types)
              │   → Local knowledge base
              │
              └── Unknown error
                  → Asks Groq's AI to explain it live
    ↓
Explanation shown in your chosen language
📦 Project Files
File	What it does
app.py	The Streamlit web interface (what you see and click)
runner.py	Safely runs your code in a separate process and catches errors
knowledge_base.py	Beginner-friendly explanations for 10 common errors in 3 languages
ai_layer.py	Calls Groq's AI API to explain any error not in the knowledge base
requirements.txt	List of Python packages needed to run the app
✨ Supported Errors (Built-in, Instant)
SyntaxError
NameError
TypeError
ValueError
IndexError
KeyError
ZeroDivisionError
IndentationError
AttributeError
FileNotFoundError

Any other error is explained live by AI.

🧰 Skills Used to Build This
Python — All the core logic
Streamlit — Turns Python code into a web app without requiring HTML, CSS, or JavaScript
subprocess, tempfile, os — Python standard libraries used to run user code in an isolated process
Regex (re) — Reads Python error messages and extracts the error type and description
Generative AI / LLMs — Groq's API explains errors that are not covered by the knowledge base
Natural Language Processing (NLP) — Generates beginner-friendly multilingual explanations
Git & GitHub — Version control and code hosting
Streamlit Community Cloud — Free public hosting with automatic deployment from GitHub
Localization — Hand-written Hindi and Marathi explanations for common errors
🚀 Run It Yourself
git clone https://github.com/Pavithra29-eng/CodeMitra.git
cd CodeMitra

python -m venv venv
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Get a free API key from Groq Console.

Then create a file:

.streamlit/secrets.toml

Add your API key:

GROQ_API_KEY = "your-key-here"

Run the app:

python -m streamlit run app.py
🌐 Deploy Your Own Copy (Free)
Push this project to your own public GitHub repository.
Go to Streamlit Community Cloud and sign in with GitHub.
Click New app.
Select your repository.
Choose the main branch.
Set the main file to app.py.
Under Settings → Secrets, add your GROQ_API_KEY.
Click Deploy.

You'll get a public link in a few minutes.

🗺️ What's Next
 Explain what a working code snippet does, not just errors
 Track error history during a session
 Read explanations aloud using text-to-speech in Hindi and Marathi
 Support more languages
 Support more programming languages such as C++, Java, and JavaScript
📄 License

MIT — free to use, modify, and share.
