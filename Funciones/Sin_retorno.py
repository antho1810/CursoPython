# Funciones
'''
Una función es un conjunto de líneas de código que realizan una tarea específica y puede retornar un valor.

Las funciones pueden tomar parámetros que modifiquen su funcionamiento.

Las funciones son utilizadas para descomponer grandes problemas en tareas simples y para implementar operaciones que
son comúnmente utilizadas durante un programa y de esta manera reducir la cantidad de código.

sintaxis:

def <nombre de la funcion> (<parametros>):
    #cuerpo de la funcion

clausula return: Las funciones pueden comunicarse con el exterior de las mismas, al proceso principal del programa
usando la sentencia return. El proceso de comunicación con el exterior se hace devolviendo valores.

tipos de argumentos
- por defecto*
- posicionales*
- nombrados*
- indefinidos*
'''
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
        imprimir("ERROR: Algo salió mal.")
        
    imprimir(f"{num1} {operacion} {num2} = {resultado}")

def Multiplicacion(num1: float, num2: float):
    multi = num1 * num2
    imprimir(f"La multiplicación de {num1} * {num2} = {multi}")

def Division(num1: float, num2: float):
    divi = num1 / num2
    imprimir(f"La division de {num1} / {num2} = {divi}")

def Suma(num1: float, num2: float):
    suma = num1 + num2
    imprimir(f"La suma de {num1} + {num2} = {suma}")

def Resta(num1: float, num2: float):
    resta = num1 - num2
    imprimir(f"La resta de {num1} - {num2} = {resta}")

def imprimir(mensaje : str):
    print(mensaje)

def main():
    Opciones(2,6, "-")


main()