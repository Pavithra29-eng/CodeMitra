"""
CodeMitra AI Layer
-------------------
Fallback explanation using Groq's free LLM API, used only when the
error type isn't in our local knowledge_base.
"""

import streamlit as st
from groq import Groq

LANGUAGE_NAMES = {
    "english": "English",
    "hindi": "Hindi",
    "marathi": "Marathi",
}


def get_ai_explanation(code: str, error_type: str, error_message: str, language: str) -> dict:
    """
    Ask Groq to explain the error in the requested language.
    Returns the same shape as knowledge_base explanations:
    {"meaning": ..., "cause": ..., "solution": ...}
    """
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    lang_name = LANGUAGE_NAMES.get(language, "English")

    prompt = f"""A beginner programmer wrote this Python code:

{code}

It raised this error:
{error_type}: {error_message}

Explain it for a total beginner in {lang_name}. Respond ONLY as JSON, no markdown, no backticks, in this exact format:
{{"meaning": "what happened, 1-2 sentences", "cause": "why it happened, 1-2 sentences", "solution": "how to fix it, 1-2 sentences"}}"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=300,
    )

    import json
    text = response.choices[0].message.content.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)