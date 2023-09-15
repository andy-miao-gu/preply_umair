from flask import Flask, render_template, request, jsonify
import openai

# Replace with your OpenAI API key
openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    openai_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"User: {user_input}\nAI:",
        temperature=0.8,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    response_text = openai_response.choices[0].text.strip()
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
