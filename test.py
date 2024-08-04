import openai
import os

# Initialize OpenAI API Key from environment variable
openai.api_key = os.getenv('sk-proj-AWNCFn8Npx35mdPI3lK2T3BlbkFJsFiYiGJSO4gvd7nxEOlB')
# if not openai.api_key:
#     raise ValueError("OPENAI_API_KEY environment variable not set")

try:
    response = openai.Completion.create(
        engine="davinci",
        prompt="Say hello!",
        max_tokens=5
    )
    print(response.choices[0].text.strip())
except Exception as e:
    print(f"Error: {e}")
