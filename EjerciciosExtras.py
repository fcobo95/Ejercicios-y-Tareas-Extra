from flask import Flask, json, jsonify, redirect, request, Response, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect('/api/welcome/', code=302)


@app.route('/api/welcome/', methods=['GET'])
def welcome_screen():
    return render_template('mainpage.html')


def params():
    return request.args


@app.route('/api/even_or_odd/', methods=['GET', 'POST'])
def determine_even_or_odd():
    param = params()

    number = param['number']

    if int(number) % 2 == 0:
        isEven = {
            'Result': 'It is Even!',
            'number': number
        }
    else:
        isEven = {
            'Result': 'It is Odd!!',
            'number': number
        }

    return Response(json.dumps(isEven), mimetype='application/json')


@app.route('/api/is_it_prime', methods=['GET'])
def is_it_prime():
    param = params()

    number = param['number']


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
