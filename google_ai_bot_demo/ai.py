import os

import google.generativeai as palm
from dotenv import load_dotenv

load_dotenv()

palm.configure(api_key=os.getenv("PALM_KEY"))


def generate(
    prompt: str, temperature: float, candidate_count: int, max_output_tokens: int
) -> str:
    return palm.generate_text(
        prompt=prompt,
        temperature=temperature,
        candidate_count=candidate_count,
        max_output_tokens=max_output_tokens,
    )
