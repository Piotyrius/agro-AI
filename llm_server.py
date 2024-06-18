from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    # Always respond with "hello"
    response_text = "hello"
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(port=5001)
