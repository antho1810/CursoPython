#Python posee tres estructuras condicionales:

#1-
#    if(<condicion>):
        #cuerpo si la condición se cumple
#2-
#    if(<condicion>):
        #cuerpo si la condición se cumple
#    else:
        #si la condicion no se cumple

#3-
#    if(<condicion>):
        #cuerpo si la condición se cumple
#    elif(<otra condicion>): # else if
        #si la condicion anterior falló y se desea evaluar otra
#    else:
        #si todo lo anterior falló

def main():
    id_gerente = "0"
    id_super = "1"
    id_administrador = "2"


    id = str(input("Ingrese su identficacion: "))

    if(id == id_gerente):
        print("Usted es gerente")
    elif(id == id_super):
        print("Usted es super usuario")
    elif(id == id_administrador):
        print("Usted es administrador")
    else:
        print("Usted no tiene permisos")

main()