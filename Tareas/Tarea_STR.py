   
   #crear variable que contenga un texto y mostrar el tipo de la variable,
   # crear otra variable que almacene la longitud de la variable anterior,
   # crear otra variable que almacene la primera variable pero en mayusculas.
   # crear otra variable que concatene la variable mayusculas y la variable de longitud

   # (+5) 

def main():

   texto = "Hola mundo"
   Upper = texto.upper()
   longitud = len(texto)
   concatena = str(longitud) + " " + Upper

   print(texto)
   print(Upper)
   print(longitud)
   print(concatena)
   print(type(texto))
main()

