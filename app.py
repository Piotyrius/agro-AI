from flask import Flask, render_template, request, redirect, url_for
import requests
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# In-memory storage for messages (for simplicity, not suitable for production)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    if user_message:
        # Add user's message to messages list
        messages.append(f"User: {user_message}")
        print(f"Received message: {user_message}")  # Print the message to the console

        try:
            # Call your local LLM API to get a response
            response = requests.post(
                'http://localhost:5001/generate',
                json={'prompt': user_message}
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            ai_message = response.json().get('response', 'No response from AI')
        except requests.RequestException as e:
            logging.error(f"Error communicating with LLM server: {e}")
            ai_message = "Error communicating with AI server."

        # Add AI's message to messages list
        messages.append(f"AI: {ai_message}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
