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

    def __str__(self):                                  # Equivalente a toString en C# o Java.
        if self.cabeza is not None:                     # Me aseguro si hay algun nodo o no.
            actual = self.cabeza                        # Asigno a Actual al primer nodo --> cabeza
            lista = 'Lista:\n' + str(actual.dato) + '\n'# Creo la vista de la lista que voy a imprimir.
            while actual.siguiente is not None:         # Mientras que el nodo actual.siguiente tenga una referencia que no sea None, sigue iterando sobre la lista.
                actual = actual.siguiente               # Avanzo en los nodos con la referencia '.siguiente' mientras que siguiente no sea None.
                lista += str(actual.dato) + '\n'        # Concateno los datos que va encontrando en los nodos a la lista.
            return lista + 'Fin de la Lista'            # Retorno la lista e imprimo que es el final de los datos de los nodos en la lista.
        return 'Lista []'                               # En caso de que la lista este vacia; que no cumpla el if, retorno una lista vacia.

if __name__ == "__main__":                              # Es mi metodo main, equivalente a la clase main(String [] args) en Java o C#.
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
