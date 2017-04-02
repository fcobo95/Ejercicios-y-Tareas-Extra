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

# Implementando una estructura de datos de Listas Simples

# ---------------------------------------------------- CLASS NODO ---------------------------------------------------- #


class Nodo(object):
    def __init__(self, dato=None, siguiente=None):          # CONSTRUCTOR DEL NODO recibe un dato y una referencia la siguiente.
        self.dato = dato                                    # Esta parte del nodo guarda la informacion o valor que le inserto.
        self.siguiente = siguiente                          # Esta parte del nodo guarda la referencia hacia el siguiente nodo.
# ---------------------------------------------------- CLASS NODO ---------------------------------------------------- #

# ---------------------------------------------------- CLASS LISTA --------------------------------------------------- #


class Lista(object):
    def __init__(self):                                     # CONSTRUCTOR DE LA LISTA recibe la referencia del primer nodo.
        self.cabeza= None                                   # conocido como primero o cabeza.
        self.ultimo = None

    def insertar_dato(self, numero):
        if self.cabeza is None:                             # Revisa si cabeza tiene algun dato, sino lo tiene, crea un nuevo nodo
            self.cabeza = Nodo(numero, None)                # Asigna el nuevo nodo a cabeza
            self.ultimo = self.cabeza                       # Se actualiza la referencia de que cabeza es igual a ultimo porque es el unico dato en la lista.

        elif self.ultimo == self.cabeza:                    # En caso de que ya exista un unico valor en la lista.
            self.ultimo = Nodo(numero, None)                # se crea un nuevo nodo.
            self.cabeza.siguiente = self.ultimo             # se actualiza el puntero.

        else:                                               # En caso de hayan mas de dos datos
            actual = Nodo(numero, None)                     # Crea un nuevo nodo donde alberga el nuevo dato
            self.ultimo.siguiente = actual                  # Como es un nuevo dato, se corre el puntero y se dice que el nodo nuevo es el nuevo ultimo
            self.ultimo = actual                            # Se actualiza el puntero.

    def length_lista(self):
        actual = self.cabeza                                # Me posicion en el primer nodo.
        contador = 0                                        # Declaro un contador para determinar el largo.
        while actual:                                       # Ciclo while para iterar sobre los nodos.
            contador += 1                                   # Por cada ocurrencia que sea cierta, le sumo 1 al contador
            actual = actual.siguiente                       # Actualizo el actual, si diera None, es falso, entonces sale del ciclo.
        return contador                                     # Retorno el largo de la lista de nodos.

    def indice(self):
        indice = 0                                          # Declaro una variable local para retornar el indice.
        nodo = self.cabeza                                  # Me ubico sobre el primer nodo de la lista.
        while nodo is not None:                             # Si el nodo existe y no es vacio haga:
            indice += 1                                     # Actualizo el valor del indice por cada dato que haya en la lista.
            return indice-1                                 # Retorno el indice y le resto uno, para que empiece desde cero y no desde 1, ya que la asignacion le suma uno al principio, entonces nunca es 0.
        return None                                         # En caso de que la lista este vacia, no existe indice.

    def determine_par_impar(self):
        nodo = self.cabeza                                  # Me coloco sobre el primer nodo, que es la cabeza
        index = self.indice()
        while nodo is not None:                             # Mientras no sea None, siga iterando sobre la lista.
            if nodo.dato % 2 == 0:                          # Si el residuo de la division del numero por numeros pares es 0, entonces es par.
                print('El numero {} es par: indice[{}]'     # Retorna este mensaje
                      .format(str(nodo.dato), str(index)))  # Retorna este mensaje si es par
            else:                                           # Sino
                print('El numero {} es impar: indice[{}]'   # Retorna este mensaje
                      .format(str(nodo.dato), str(index)))  # Retorna este mensaje
            index += 1
            nodo = nodo.siguiente                           # Actualizo mi posicion del puntero sobre la lista.
                                                            # No necesito retornar nada, ya que solo quiero saber que dato es par y cual no
                                                            # y ya imprime cuales si son y cuales no.

    def reste_n(self, number):
        nodo = self.cabeza                                  # Me ubico en el primer nodo de la lista.
        while nodo is not None:                             # Mientras que el nodo no sea None, siga iterando.
            resultado = nodo.dato - number                  # Variable local resultado para imprimir el resultado de la resta al dato de ese nodo.
            print('{} - {} = {}'                  # Imprimo el numero original, y el resultado de la resta.
                  .format(nodo.dato, number, resultado))
            nodo = nodo.siguiente                           # Actualizo el puntero y sigo iterando, mientras no sea None

    def raiz_cuadrada(self):
        nodo = self.cabeza                                  # Me ubico en el primer nodo de la lista.
        while nodo is not None:                             # Mientras que la referencia del nodo no sea None, siga.
            cuadrado = nodo.dato ** (1/2)                   # Variable local cuadrado para almacenar el resultado de la raiz cuadrada del dato de ese nodo.
            print('La raiz cuadrada de {} es {}'            # Imprimo el numero y su raiz cuadrada.
                  .format(str(nodo.dato), str(cuadrado)))
            nodo = nodo.siguiente

    def __str__(self):                                      # Equivalente a toString en C# o Java.
        if self.cabeza is not None:                         # Me aseguro si hay algun nodo o no.
            actual = self.cabeza                            # Asigno a Actual al primer nodo --> cabeza
            lista = 'Lista:\n' + str(actual.dato) + '\n'    # Creo la vista de la lista que voy a imprimir.
            while actual.siguiente is not None:             # Mientras que el nodo actual.siguiente tenga una referencia que no sea None, sigue iterando sobre la lista.
                actual = actual.siguiente                   # Avanzo en los nodos con la referencia '.siguiente' mientras que siguiente no sea None.
                lista += str(actual.dato) + '\n'            # Concateno los datos que va encontrando en los nodos a la lista.
            return lista + 'Fin de la Lista'                # Retorno la lista e imprimo que es el final de los datos de los nodos en la lista.
        return 'Lista []'                                   # En caso de que la lista este vacia; que no cumpla el if, retorno una lista vacia.
# ---------------------------------------------------- CLASS LISTA --------------------------------------------------- #
#                                                                                                                      #
# -------------------------------------------------------- MAIN ------------------------------------------------------ #
if __name__ == "__main__":              # Es mi metodo main, equivalente a la clase main(String [] args) en Java o C#.
    Listas = Lista()                    # Creo una instancia de la clase Lista
    # for numero in range(1, 1000):       # Le ingreso datos en un rango de 1 ==> 1000
    #     Listas.insertar_dato(numero)    # Inserto los datos en la lista
    import random
    for numero in range(1000):
        numeros = random.randint(1, 1000)
        Listas.insertar_dato(numeros)
    print(Listas)                       # Imprimo la lista.
    print('Tamaño de la lista')
    print(Listas.length_lista())        # Imprimo el tamaño de la lista.
    print('Fin tamaño de la lista')
    Lista.determine_par_impar(Listas)   # Imprime que numeros son pares, y cuales no.
    Lista.raiz_cuadrada(Listas)         # Imprime la raiz cuadra de cada numero en la lista.
    Lista.reste_n(Listas, 50)           # Resta por la cantidad en el segundo argumento sobre los valores de los datos de la lista.
