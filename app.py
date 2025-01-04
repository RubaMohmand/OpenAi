from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv
import os

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({"error": "Question is required"}), 400

    try:
        # Using the updated OpenAI API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Replace with the desired model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=150
        )
        answer = response['choices'][0]['message']['content'].strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
