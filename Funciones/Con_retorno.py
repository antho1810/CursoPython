'''
las funciones que retornan, en otros lenguajes, se caracterizan por tener un tipo especificado en la definición.

Esto no pasa en python. Aquí las funciones pueden retornar o no un valor, dependiendo de la situación y del contexto de
la función.

Las funciones que retornan están definidas por la clausula "return" en el cuerpo de la misma. Si se especifica al menos
return dentro de la función, sí o sí, esta debe retornar algún valor.

Estas funciones devuelven un valor y, si no se almacena en una variable o estructura de datos, se perderá el valor. Por
lo tanto, debemos asegurarnos de que el valor sea inyectado en otra variable.
'''
def sayHello(name:str) -> str:
    return f"Hello (name)"


def rango(num: int) -> [int]:
    array = [0]*num

    valorActual = 0
    for i in range(len(array)):
        
        array[i] = valorActual
        valorActual += 1
    return array
def suma(nm1:float, nm2: float) -> float:
    return nm1 + nm2

def Opciones(num1: float, num2: float, operacion: str):
    resultado = 0
    if (operacion == "+"):
        resultado = num1 + num2
    elif (operacion == "-"):
        resultado = num1 - num2
    elif (operacion == "*"):
        resultado = num1 * num2
    elif (operacion == "/" and num2 != 0):
        resultado = num1 / num2
    else:
        return "ERROR: Algo salió mal."
        
        
    return f"{num1} {operacion} {num2} = {resultado}"

def main():
    '''
    saludo = sayHello("Anthony")
    print(saludo)
    print(sayHello("Anthony"))
'''

    suma = Opciones(2, 2, "+")
    print(suma)

'''
    print(rango(5))
    for i in range(10): 
        print(i)
'''
main()