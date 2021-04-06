'''
Se usa para iterar sobre una secuencia de elementos

for <var index> in range(<inicio iteracion>,<final iteracion-1>):
    #codigo a repetir

Se puede iterar sobre alguna lista o se puede usar la función range() para
generar un rango de valores los cuales, nuestra variable indexadora, tomará

Tambien se puede iterar sobre cadenas
'''

def main():
    for i in range(2):
        print(i)
        
    #pass: ingenorar este ciclo
    #for <var index> in range( <inicio: numero>, <final: numero>, <incremento: numero):

main()