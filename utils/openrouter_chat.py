# utils/openrouter_chat.py
from google import genai
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

def call_openrouter(prompt: str, model: str = "google/gemini-2.5-flash-lite-preview-06-17") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error calling OpenRouter: {e}"

# def call_openrouter(prompt: str, model: str = "google/gemini-2.5-flash-lite-preview-06-17") -> str:

#     client = genai.Client(api_key='')

#     response = client.models.generate_content(
#         model="gemini-2.5-flash", contents=prompt
#     )
#     return response.text
