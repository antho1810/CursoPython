def main():
 V1 = int(input("Ingrese el primer valor: "))
 V2 = int(input("Ingrese el segundo valor: "))

 for i in range(V1, V2):
     if i % 2 != 0:
         print(i)
main()