import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

url = "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}
history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "coder",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = json.loads(response.text)
        actual_response = data['response']
        return actual_response
    else:
        print("Error:", response.text)
        return "Error generating response."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        response = generate_response(user_prompt)
        return render_template('index.html', response=response, prompt=user_prompt)

    return render_template('index.html', response='', prompt='')

if __name__ == '__main__':
    app.run(debug=True)
