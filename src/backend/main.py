from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI
from dotenv import dotenv_values

from flask import Flask, jsonify, request
server = Flask(__name__)
CORS(server)

config = dotenv_values(".env")
client = OpenAI(api_key = config['api'])

def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()

def generate(prompt: str, document: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            { 
                "role": "user",
                "content": prompt + document + '[Output]:'
            }],
        stream=False,
    ).choices[0].message.content
    return str(response)

@server.route('/generate', methods=['POST'])
def test():
    text = request.get_json()['text']
    print("user sent", text)
    generation = generate(read_file("prompt.txt"), text)
    print("THE RESULT IS",generation)

    return jsonify({'result': generation})


if __name__ == '__main__':
    server.run(debug=True, port=8000)