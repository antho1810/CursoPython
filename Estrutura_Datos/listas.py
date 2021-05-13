'''
las listas son estructuras de datos que se usan para almacenar valores.
Se asemejan a los vectores

Append(<obj>)
    Este método nos permite agregar nuevos elementos a una lista/vector.

Remove(<indice>)
    El método remove va a remover un elemento que se le pase como
    parámentro de la lista a donde se le esté aplicando.

Index(<dato>)
    Index devuelve el número de indice del elemento que le pasemos por parámetro.

Count(<dato>)
    Para saber cuántas veces un elemento de una lista
    se repite podemos utilizar el metodo count().

Reverse()
    También podemos invertir los elementos  de una lista.
'''
def main():

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listaLetra = ['a', 'b', 'c', 'd']
    lista.reverse()
    
    print(listaLetra.count('c'))
    listaLetra.remove('b')
    lista.remove(4)
    print(lista)
    print(listaLetra)
    print(listaLetra.index('d'))

main()