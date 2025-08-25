"""
Service: chatbot – minimal wrapper over OpenAI Chat Completions.

Requires OPENAI_API_KEY env var and the openai package installed:
  poetry add openai
"""
from __future__ import annotations


def chat_once(prompt: str, model: str = "gpt-4o-mini") -> str:
    """
    Send a single user prompt and return the assistant's reply text.
    """
    try:
        import openai  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("chatbot requires 'openai' (poetry add openai)") from exc

    client = openai.OpenAI()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content  # type: ignore[return-value]
