# Indicaciones
"""
1. Crear  y alimentar un vector, 1000 elementos tipo double.
        a. Crear un método que calcule las raíces cuadradas de cada entrada del arreglo
        b. Crear un método que reste n unidades a cada entrada del arreglo
2. Crear y alimentar un vector de números enteros generados aleatoriamente.
        a. Obtener un rango de elementos de dicho vector, donde el rango está dado por el índice a y b tomando en cuenta que rango no debe superar las dimensiones del arreglo.
        b. Obtener los números primos que se encuentra en el arreglo
        c. Obtener los números pares e impares
                i. Se devuelve el índice
                ii. Se devuelve el numero
        d. Invertir arreglo
                i. Se invierte el orden del arreglo, esto es si se tiene el arreglo: [a,b,c,d,r,f,g,] la salida de invertir seria: [g,f,r,d,c,d,a]
        e. Obtener el Largo de un Arreglo:
                i. [g,f,r,d,c,d,a] -> 6
                ii. [] -> 0
        f. Obtener el elemento medio de un arreglo
Devuelve la posición largo/2 del arreglo en caso de no ser división entera devuelve la posición largo-1/2
3. Eliminar el primer elemento un vector:
Entrada: [a,b,n,m,x,]

Salida: [b,n,m,x,]
"""


# -------------------- CLASS FloatArray BEGINS ----------------------------------------------------------------------- #
class FloatArray:
    # self means that the constructor is taking in the instance of that object.
    # self is always taken as the first argument in the constructor parameters
    def __init__(self):
        self.the_array = []
        self.the_result_array = []

    def fill_array(self):
        for each_number in range(20):
            self.the_array.append(each_number)

    def format(self, x, y):
        return print('{} : {}'.format(x, y))

    # This method will handle how to calculate the square root of 1000 numbers that go into an array.
    def square_root(self):
        print('This prints the square root for each number in the array.')
        for each_number in self.the_array:
            try:
                square_root = each_number ** (1 / 2)
                self.the_result_array.append(square_root)
                self.format(each_number, square_root)
            except Exception as ex:
                return 'Something went wrong: ' + str(ex)
        return ''

    def subtract(self, number1, number2):
        return number1 - number2

    def subtract_n_from_array(self, take_away):
        for each_number in self.the_array:
            new_number = self.subtract(each_number, take_away)
            self.format(each_number, new_number)
        return 'Succesful operation'


# -------------------- CLASS FloatArray ENDS ------------------------------------------------------------------------- #
# Instance of FloatArray class
floatClass = FloatArray()
print('---------------BEGIN OF FLOATARRAY CLASS---------------' + '\n')
FloatArray.fill_array(floatClass)
FloatArray.square_root(floatClass)
FloatArray.subtract_n_from_array(floatClass, 10)
print('---------------END OF FLOATARRAY CLASS---------------' + '\n')


# -------------------- CLASS IntegerArray BEGINS --------------------------------------------------------------------- #
class IntegerArray:
    def __init__(self):
        self.the_array = []
        self.the_result_array = []

    def length(self):
        self.cont = 0
        for each_number in self.the_array:
            self.cont += 1
        return print(self.cont)

    def isEven(self, each_number):
        if each_number % 2 == 0:
            return each_number

        return
    def even_number(self):
        for each_number in self.the_array:
            if self.isEven(each_number):
                print('It\'s an even number: ' + str(each_number))
            else:
                print('It\'s an odd number: ' + str(each_number))
        return each_number

    def vector(self):
        import random
        for each_number in range(20):
            try:
                self.the_array.append(random.randint(1, 100))
            except Exception as ex:
                return 'Something went wrong: ' + str(ex)


# -------------------- CLASS IntegerArray ENDS ----------------------------------------------------------------------- #
# Instance of IntegerArray class
intClass = IntegerArray()
print('---------------BEGIN OF INTEGERARRAY CLASS---------------' + '\n')
IntegerArray.vector(intClass)
IntegerArray.even_number(intClass)
print('Size of the array: ')
IntegerArray.length(intClass)
print('---------------END OF INTEGERARRAY CLASS---------------' + '\n')
