"""
crear un programa que le pida al usuario su edad, nombre, dos números y muestre por pantalla:
    - suma
    - resta
    - multiplicación
    - o división (dependiendo de la opcion)
    - de ambos números seguidos de su nombre y edad
    NOTA: si el usuario no es mayor de 5 años, no puede usar el programa
"""

'''
    ingrese su nombre
    ingrese su edad
    ingrese el primer numero 
    ingrese el segundo numero 

    1. suma
    2. resta
    3. multi
    4. division
    resultado de la operación : X 
    Nombre: 
    Edad: 
    
'''
def main():
    suma = "1"
    resta = "2"
    multiplicación = "3"
    division = "4"
    exponente = "5"

    nombre = str(input("Ingrese su nombre: "))
    edad = str(input("Ingrese su edad: "))
    V1 = int(input("Ingrese el primer valor: "))
    V2 = int(input("Ingrese el segundo valor: "))
    id = input("1-suma\n2-resta\n3-multiplicacion\n4-division\n5-exponente\nopcion: ")
    print("Su resultado es: ")

    if(id == suma):
        print(V1 + V2)
    elif(id == resta):
        print(V1 - V2)
    elif(id == multiplicación):
        print(V1 * V2)
    elif(id == division):
        print(V1 / V2)
    elif(id == exponente):
        print(V1 ** V2)
    else:
        print("Error")
    
    print("Su nombre es: " + nombre)
    print("Su edad es: "+ edad)

    
main()