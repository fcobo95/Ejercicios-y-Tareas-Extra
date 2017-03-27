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


# @app.route('/api/is_it_prime', methods=['GET'])
# def is_it_prime():
#     param = params()
#
#     number = param['number']

# Tarea Vectores Erick Fernando Cobo Enriquez 3/27/2017
import random

vector = []

# Falta agregar la ruta.
# Este metodo se va a encargar de calcular cada una de las raices cuadradas para cada numero dentro del vector.
def square_roots():
    number = 0
    sqrt = 0
    # Con esto lleno el vector
    for i in range(1000):
        vector.append(float(i))
    # Aqui calculo para cada numero del vector cual es su raiz cuadrada
    for number in vector:
        sqrt = number ** (1 / 2)
        print("The number is: " + str(number) + " and its square root is: " + str(sqrt))
    return sqrt

#def
square_roots()



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
