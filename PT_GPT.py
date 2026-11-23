"""Minimal Groq chat example.

Setup:
    pip install -r requirements.txt
    Set the GROQ_API_KEY environment variable before running this file.
"""

import os
import sys

try:
    from groq import Groq
except ImportError:
    print(
        "Missing dependency: install it with `python -m pip install -r requirements.txt`.",
        file=sys.stderr,
    )
    raise


MODEL = "openai/gpt-oss-20b"


def main() -> None:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Set it as an environment variable before running."
        )

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "Say hello in one sentence."}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
