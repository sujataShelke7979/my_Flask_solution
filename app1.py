from flask import Flask, request, jsonify
from flask_limiter import Limiter
import openai

app = Flask(__name__)

# Set OpenAI API key (replace with your actual OpenAI API key)
openai.api_key = "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"

# Function to generate the biodata outline using OpenAI
def gen_outline(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose a suitable model for your needs
        prompt=f"{input_text}\nGenerate biodata outline:",
        temperature=0.7,
        max_tokens=200
    )
    biodata_outline = response['choices'][0]['text'].strip()
    return biodata_outline

# API endpoint to generate biodata outline
@app.route('/generate', methods=['GET'])
def gen_bio_outline():
    data = request.json
    if data and 'command' in data and data['command'] == 'generate an outline for biodata':
        if 'input_text' in data:  # Assuming the user provides input_text in the JSON request
            try:
                biodata_outline = gen_outline(data['input_text'])
                return jsonify({"output": biodata_outline}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "Missing 'input_text' in JSON request"}), 400
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run()
