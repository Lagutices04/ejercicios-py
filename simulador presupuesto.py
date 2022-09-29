presupuesto=100000
gastoc=0
#gasto es igual a acumulado restando
total=0
#total es el contador sumando
repetir="s"
gasto=input("si desea seguir ingrese S o s,si quiere terminar N")
while repetir=="s" or repetir=="S":
   gasto=int(input("registre un gasto"))
   gastoc=gastoc+1
   presupuesto=presupuesto-gasto
   print(f"tu  gasto es {gasto} ")
   print(f"el presupuesto que te queda es{presupuesto}")
   
   if gasto>=100000:
      print("no puedes ingresar mas datoss")
   else:
      print("has superado el limite de gastos")

    
    
from random import randint


print (" tu compra debe ser mayor de $50000\n")

  

compra= int(input("indique el valor de su compra\n"))
print(" la bolita roja obtienen el 10 de descuento \n la bolita azul obtiene un 30 de desdcuento \n la bolita amarilla un 50 de descuento \n la bolita blanca un 100 de la compra gratis \n" )



br=compra*10/100
ba=compra*30/100
bam=compra*50/100
bbl=compra


bola= randint(1,4)
 
print(bola)
if  bola == 1 and br :
    print(input( f"recibiste el descuento de $ {br}\n "))
elif bola == 2 and ba:
    print(input( f"recibiste el descuento de $ {ba}\n"))
elif bola == 3 and bam:
    print(input( f"recibiste el descuento de $ {bam}\n "))
elif bola == 4 and bbl:
    print(input(f"tu compra se gastis !felicitaciones¡ {bbl}\n "))       
elif compra < 50000: 
    print("no aplicas al dscuento")   
else:
    print("los datos son incorrectos ") 
