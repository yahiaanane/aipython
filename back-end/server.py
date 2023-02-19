import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY_HERE"

@app.route('/chatgpt', methods=['POST'])
def chat_gpt():
    data = request.get_json()
    prompt = data['prompt']
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return jsonify(choices=completions.choices)

if __name__ == '__main__':
    app.run(debug=True)
