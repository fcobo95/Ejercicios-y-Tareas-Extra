from flask import Flask, json, jsonify, redirect, request, Response, render_template

app = Flask(__name__)

class ejercicios_extra:
    @app.route('/')
    def hello_world(self):
        return redirect('/api/welcome/', code=302)


    @app.route('/api/welcome/', methods=['GET'])
    def welcome_screen(self):
        return render_template('mainpage.html')


    def params(self):
        return request.args


    @app.route('/api/even_or_odd/', methods=['GET', 'POST'])
    def determine_even_or_odd(self):
        ejercicios = ejercicios_extra

        param = ejercicios.params(self)

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

class tareas_servicios_web:
    # This method will handle how to calculate the square root of 1000 numbers that go into an array.
    def float_square_roots(self):
        the_result_array = []
        the_array = []
        # I fill the_array with float values
        for each_value in range(1000):
            the_array.append(float(each_value))
        """
        I iterate through all the values of "the_array" and calculate their respective square root value
        it then appends it to "the_result_array" and transforms it into a Dictionary.
        """
        for each_number in the_array:
            square_root = each_number ** (1 / 2)
            print(the_result_array.append({
                "Number": each_number,
                "Square Root": square_root
            }))

        return the_result_array



    def integer_square_roots(self):
        the_result_array = []
        the_array = []
        import random
        for each_number in range(random.randrange(0,1000)):

tareas = tareas_servicios_web
tareas.float_square_roots()
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')
