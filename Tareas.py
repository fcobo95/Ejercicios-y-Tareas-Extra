# # Indicaciones
# """
# 1. Crear  y alimentar un vector, 1000 elementos tipo double.
#         a. Crear un método que calcule las raíces cuadradas de cada entrada del arreglo
#         b. Crear un método que reste n unidades a cada entrada del arreglo
# 2. Crear y alimentar un vector de números enteros generados aleatoriamente.
#         a. Obtener un rango de elementos de dicho vector, donde el rango está dado por el índice a y b tomando en cuenta que rango no debe superar las dimensiones del arreglo.
#         b. Obtener los números primos que se encuentra en el arreglo
#         c. Obtener los números pares e impares
#                 i. Se devuelve el índice
#                 ii. Se devuelve el numero
#         d. Invertir arreglo
#                 i. Se invierte el orden del arreglo, esto es si se tiene el arreglo: [a,b,c,d,r,f,g,] la salida de invertir seria: [g,f,r,d,c,d,a]
#         e. Obtener el Largo de un Arreglo:
#                 i. [g,f,r,d,c,d,a] -> 6
#                 ii. [] -> 0
#         f. Obtener el elemento medio de un arreglo
# Devuelve la posición largo/2 del arreglo en caso de no ser división entera devuelve la posición largo-1/2
# 3. Eliminar el primer elemento un vector:
# Entrada: [a,b,n,m,x,]
#
# Salida: [b,n,m,x,]
# """
#
#
# # EJERCICIO #1
# # -------------------- CLASS FloatArray BEGINS ----------------------------------------------------------------------- #
# class FloatArray:
#     # self means that the constructor is taking in the instance of that object.
#     # self is always taken as the first argument in the constructor parameters
#     def __init__(self):
#         self.the_array = []
#         self.the_result_array = []
#
#     def fill_array(self):
#         for each_number in range(50):
#             self.the_array.append(each_number)
#
#     def format(self, x, y):
#         return print('{} : {}'.format(x, y))
#
#     # This method will handle how to calculate the square root of 1000 numbers that go into an array.
#     def square_root(self):
#         print('This prints the square root for each number in the array.')
#         for each_number in self.the_array:
#             try:
#                 square_root = each_number ** (1 / 2)
#                 self.the_result_array.append(square_root)
#                 self.format(each_number, square_root)
#             except Exception as ex:
#                 return 'Something went wrong: ' + str(ex)
#         return ''
#
#     def subtract(self, number1, number2):
#         return number1 - number2
#
#     def subtract_n_from_array(self, take_away):
#         for each_number in self.the_array:
#             new_number = self.subtract(each_number, take_away)
#             self.format(each_number, new_number)
#         return 'Succesful operation'
#
#
# # Instance of FloatArray class
# floatClass = FloatArray()
# print('---------------BEGIN OF FLOATARRAY CLASS---------------' + '\n')
# FloatArray.fill_array(floatClass)
# FloatArray.square_root(floatClass)
# FloatArray.subtract_n_from_array(floatClass, 10)
# print('---------------END OF FLOATARRAY CLASS---------------' + '\n')
#
#
# # -------------------- CLASS FloatArray ENDS ------------------------------------------------------------------------- #
#
#
# # EJERCICIO #2
# # -------------------- CLASS IntegerArray BEGINS --------------------------------------------------------------------- #
# class IntegerArray:
#     def __init__(self):
#         self.the_array = []
#         self.the_result_array = []
#
#     def length(self):
#         self.cont = 0
#         for each_number in self.the_array:
#             self.cont += 1
#         return print(self.cont)
#
#     def isEven(self, each_number):
#         if each_number % 2 == 0:
#             return each_number
#
#         return
#
#     def isPrime(self, each_number):
#         if each_number % 2 != 0:
#             if each_number % 3 != 0:
#                 if each_number % 5 != 0:
#                     if each_number % 7 != 0:
#                         return each_number
#
#     def check_for_even_numbers(self):
#         for each_number in self.the_array:
#             if self.isEven(each_number):
#                 print('It\'s an even number: ' + str(each_number))
#             else:
#                 print('It\'s an odd number: ' + str(each_number))
#
#     def check_for_prime_numbers(self):
#         for each_number in self.the_array:
#             if self.isPrime(each_number):
#                 print('It\'s a prime number: ' + str(each_number))
#             else:
#                 print('It\'s not a prime number: ' + str(each_number))
#
#     def vector(self):
#         import random
#         for each_number in range(20):
#             try:
#                 self.the_array.append(random.randint(1, 20))
#             except Exception as ex:
#                 return 'Something went wrong: ' + str(ex)
#
#
# # Instance of IntegerArray class
# intClass = IntegerArray()
# print('---------------BEGIN OF INTEGERARRAY CLASS---------------' + '\n')
# IntegerArray.vector(intClass)
# # IntegerArray.check_for_even_numbers(intClass)
# IntegerArray.check_for_prime_numbers(intClass)
# print('Size of the array: ')
# IntegerArray.length(intClass)
# print('---------------END OF INTEGERARRAY CLASS---------------' + '\n')


# -------------------- CLASS IntegerArray ENDS ----------------------------------------------------------------------- #

# Implementando una estructura de datos de Listas Simples
class Nodo(object):
    def __init__(self, dato = None, siguiente = None):  # CONSTRUCTOR DEL NODO recibe un dato y una referencia la siguiente.
        self.dato = dato                                # Esta parte del nodo guarda la informacion o valor que le inserto.
        self.siguiente = siguiente                      # Esta parte del nodo guarda la referencia hacia el siguiente nodo.

class Lista(object):
    def __init__(self):                                 # CONSTRUCTOR DE LA LISTA recibe la referencia del primer nodo.
        self.cabeza= None                               # conocido como primero o cabeza.
        self.ultimo = None

    def insertar(self, numero):
        if self.cabeza is None:                         # Revisa si cabeza tiene algun dato, sino lo tiene, crea un nuevo nodo
            self.cabeza = Nodo(numero, None)            # Asigna el nuevo nodo a cabeza
            self.ultimo = self.cabeza                   # Se actualiza la referencia de que cabeza es igual a ultimo porque es el unico dato en la lista.

        elif self.ultimo == self.cabeza:                # En caso de que ya exista un unico valor en la lista.
            self.ultimo = Nodo(numero, None)            # se crea un nuevo nodo.
            self.cabeza.siguiente = self.ultimo         # se actualiza el puntero.

        else:                                           # En caso de hayan mas de dos datos
            actual = Nodo(numero, None)                 # Crea un nuevo nodo donde alberga el nuevo dato
            self.ultimo.siguiente = actual              # Como es un nuevo dato, se corre el puntero y se dice que el nodo nuevo es el nuevo ultimo
            self.ultimo = actual                        # Se actualiza el puntero.

    def __str__(self):
        if self.cabeza is not None:
            actual = self.cabeza
            lista = 'Lista:\n' + str(actual.dato) + '\n'
            while actual.siguiente is not None:
                actual = actual.siguiente
                lista += str(actual.dato) + '\n'
            return lista + 'Fin de la Lista'
        return 'Lista [vacia]'

if __name__ == "__main__":
    Listas = Lista()
    Listas.insertar(1)
    Listas.insertar(2)
    Listas.insertar(3)
    Listas.insertar(4)
    Listas.insertar(5)
    Listas.insertar(6)
    Listas.insertar(7)
    Listas.insertar(8)
    Listas.insertar(9)
    Listas.insertar(10)
    Listas.insertar(11)
    Listas.insertar(12)
    Listas.insertar(13)
    Listas.insertar(14)
    Listas.insertar(15)

    print(Listas)
