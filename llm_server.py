from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Fetch the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=50
        )
        response_text = response.choices[0].text.strip()
        return jsonify({'response': response_text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'response': f"Error: {e}"}), 500

if __name__ == '__main__':
    app.run(port=5001)
