import random 


print (" tu apuesta debe ser mayor de $10000")
valor=int(input("ingrese el valor que desee apostar"))
valor=0
 
apuesta=random.randint(1,2)
if valor<=10000:
    print("no puedes apostar")
elif apuesta==1:
   lado='cara'
elif apuesta==2:
   lado='cruz'
else:
    ("ingreso valores incorrectos")


print ("quieres cara o cruz")
respuesta=input()

if respuesta==lado:
   print(f'¡Muy bien,  ha salido {lado}, has acertado!')
  

elif respuesta!=lado:
   print(f'¡Mala suerte,  ha salido {lado}, has perdido!')
else:
    ("valores incorrectos")