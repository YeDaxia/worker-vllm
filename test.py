import os

from openai import OpenAI


runpod_api_key = os.getenv("RUNPOD_API_KEY")
runpod_base_url = os.getenv("RUNPOD_BASE_URL", "https://api.runpod.ai/v2/9old3k61xkum3u/openai/v1")

if not runpod_api_key:
    raise RuntimeError("Please set RUNPOD_API_KEY before running this script.")

client = OpenAI(
    api_key=runpod_api_key,
    base_url=runpod_base_url,
)

response = client.chat.completions.create(
    model="google/gemma-4-E2B-it",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, who are you?"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)