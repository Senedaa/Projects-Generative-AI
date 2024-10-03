import os
from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv  # Added to load environment variables from a .env file

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI API with your key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    user_question = request.form['question']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_question}]
    )
    return jsonify(response=response['choices'][0]['message']['content'].strip())

if __name__ == '__main__':
    app.run(debug=True)
