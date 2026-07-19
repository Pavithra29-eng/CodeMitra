"""
CodeMitra Runner
----------------
Executes user-submitted Python code in an isolated subprocess (not in-process
exec) so that a crashing or malicious script cannot affect the Streamlit app
itself. Captures stdout, stderr, and parses the error type/message if the
code raises an exception.
"""

import subprocess
import sys
import tempfile
import os
import re

TIMEOUT_SECONDS = 5


def run_code(code: str) -> dict:
    """
    Run the given Python code in a subprocess.

    Returns a dict:
        {
            "success": bool,
            "stdout": str,
            "stderr": str,          # full raw traceback text
            "error_type": str|None,
            "error_message": str|None,
        }
    """
    result = {
        "success": False,
        "stdout": "",
        "stderr": "",
        "error_type": None,
        "error_message": None,
    }

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        proc = subprocess.run(
            [sys.executable, tmp_path],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
        result["stdout"] = proc.stdout
        result["stderr"] = proc.stderr

        if proc.returncode == 0:
            result["success"] = True
        else:
            error_type, error_message = _parse_traceback(proc.stderr)
            result["error_type"] = error_type
            result["error_message"] = error_message

    except subprocess.TimeoutExpired:
        result["stderr"] = f"Execution timed out after {TIMEOUT_SECONDS} seconds."
        result["error_type"] = "TimeoutError"
        result["error_message"] = "The code took too long to run (possible infinite loop)."

    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass

    return result


def _parse_traceback(stderr: str):
    """
    Extract the error type and message from a Python traceback string.
    E.g. "NameError: name 'x' is not defined" -> ("NameError", "name 'x' is not defined")
    """
    if not stderr.strip():
        return None, None

    lines = [line for line in stderr.strip().splitlines() if line.strip()]
    last_line = lines[-1] if lines else ""

    match = re.match(r"^([A-Za-z_][A-Za-z0-9_.]*)\s*:\s*(.*)$", last_line)
    if match:
        return match.group(1), match.group(2)

    # SyntaxError sometimes reports without a clean "Type: message" on the last line
    for line in reversed(lines):
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_.]*Error)\s*:\s*(.*)$", line)
        if match:
            return match.group(1), match.group(2)

    return "UnknownError", last_line
