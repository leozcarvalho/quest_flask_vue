from flask import Flask, jsonify, request
from flask_cors import CORS

RESULTS = [
{
    #'answers': ["sim", "nao", "nao", "nao", "nao"],
    'result': 'Inocente'
}
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/result', methods=['GET'])
def get_result():
    response_object = {'status': 'success'}
    response_object['result'] = RESULTS
    return jsonify(response_object)

@app.route('/result', methods=['POST'])
def set_result():
    post_data = request.get_json()
    answers = post_data['answers']

    yesAnswers = answers.count('sim')

    if yesAnswers == 0:
        result = 'Inocente'

    if yesAnswers == 2:
        result = 'Suspeito'
    
    if yesAnswers >= 3 and yesAnswers <= 4:
        result = 'Cúmplice'

    if yesAnswers == 5:
        result = 'Assassino'

    response_object = {'result': result}
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()