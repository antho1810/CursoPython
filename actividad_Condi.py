def main():
    C1 = str(input("Ingrese el primer numero: "))
    C2 = str(input("Ingrese el segundo numero: "))

    if(C1 > C2):
        print("el numero mayor es: "+ C1 or C2)
       
    elif(C1 < C2):
        print("el numero menor es: "+ C2 or C1)
        
    elif(C1 == C2):
         print("Son iguales")
        

main()