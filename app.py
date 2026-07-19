"""
CodeMitra - Multilingual Programming Error Explainer
=====================================================
Run with: streamlit run app.py
"""

import streamlit as st
from knowledge_base import LANGUAGES, get_explanation
from runner import run_code

st.set_page_config(page_title="CodeMitra", page_icon="🚀", layout="centered")

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("💻 CodeMitra")
st.caption("Understand Python errors in your own language — English, Hindi, or Marathi.")

# ---------------------------------------------------------------------------
# Sidebar controls
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("Settings")
    language_key = st.selectbox("Select Language", list(LANGUAGES.keys()))
    st.markdown("---")
    st.markdown(
        "**Supported errors:**\n\n"
        "SyntaxError, NameError, TypeError, ValueError, IndexError, "
        "KeyError, ZeroDivisionError, IndentationError, AttributeError, "
        "FileNotFoundError"
    )
    st.markdown("---")
    st.markdown("Made with ❤️ for beginner programmers.")

# ---------------------------------------------------------------------------
# Sample snippets to make first-run easy
# ---------------------------------------------------------------------------
SAMPLES = {
    "-- Choose an example --": "",
    "NameError example": "print(name)",
    "ZeroDivisionError example": "a = 10\nb = 0\nprint(a / b)",
    "IndexError example": "items = [1, 2, 3]\nprint(items[5])",
    "TypeError example": "print('5' + 5)",
}

sample_choice = st.selectbox("Or load an example:", list(SAMPLES.keys()))
default_code = SAMPLES[sample_choice] if sample_choice != "-- Choose an example --" else "print(name)"

# ---------------------------------------------------------------------------
# Code input
# ---------------------------------------------------------------------------
st.subheader("Enter Python Code")
code = st.text_area("Your code:", value=default_code, height=180, label_visibility="collapsed")

run_clicked = st.button("▶️ Run Code", type="primary")

# ---------------------------------------------------------------------------
# Execution + explanation
# ---------------------------------------------------------------------------
if run_clicked:
    if not code.strip():
        st.warning("Please enter some Python code first.")
    else:
        with st.spinner("Running your code..."):
            result = run_code(code)

        if result["success"]:
            st.success("✅ Code ran successfully — no errors!")
            if result["stdout"]:
                st.subheader("Output")
                st.code(result["stdout"], language="text")
        else:
            error_type = result["error_type"] or "UnknownError"
            st.error(f"❌ Error Detected: {error_type}")

            explanation = get_explanation(error_type, language_key)

            st.subheader("📖 Explanation")
            st.markdown(f"**What happened?**\n\n{explanation['meaning']}")
            st.markdown(f"**Why did this happen?**\n\n{explanation['cause']}")

            st.subheader("💡 Solution")
            st.markdown(explanation["solution"])

            with st.expander("Show raw error (technical details)"):
                st.code(result["stderr"] or f"{error_type}: {result['error_message']}", language="text")

st.markdown("---")
st.caption(
    "CodeMitra runs your code in an isolated process with a 5-second timeout. "
    "Avoid running untrusted code from others."
)
