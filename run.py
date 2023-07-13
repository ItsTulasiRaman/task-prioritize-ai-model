from flask import Flask, Response, jsonify
from ai_prompt import generate_prompt,input_text_update

app = Flask(__name__)


@app.route("/usage/api/prompt")
def index():
    return Response (generate_prompt(),status=200)


@app.route("/usage/api/prompt/update/<input>",methods=['POST'])
def update(input):
    return Response(input_text_update(input),status=200)



if __name__ == '__main__':
    app.run()