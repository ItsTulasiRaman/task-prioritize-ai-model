from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route('/askgpt', methods=['POST'])
def ask_gpt():
    message = request.form.get('Message')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a task manager. Prioritize the tasks in terms of importance"},
            {"role": "user", "content": message}
        ]
    )

    generated_message = completion.choices[0].message['content']
    generated_message = generated_message.encode().decode('unicode_escape')

    return jsonify({'message': generated_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
