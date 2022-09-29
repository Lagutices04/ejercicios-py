#supermercados noe 



from random import randint

presupuesto=10000000000000000000000
gastoc=0
#gasto es igual a acumulado restando
total=0
#total es el contador sumando

print (" tu compra debe ser mayor de $50000\n")
gasto= int(input("indique el valor de su compra\n"))
gastoc=gastoc+1
presupuesto=presupuesto-gasto
print(f"tu  gasto es {gastoc} ")
print(f"el presupuesto que te queda es{presupuesto}")

print(" la bolita roja obtienen el 10 de descuento \n la bolita azul obtiene un 30 de desdcuento \n la bolita amarilla un 50 de descuento \n la bolita blanca un 100 de la compra gratis \n" )
print (" tu compra debe ser mayor de $50000\n")

  

compra= int(input("indique el valor de su compra\n"))


br=compra*10/100
ba=compra*30/100
bam=compra*50/100
bbl=compra


bola= randint(1,4)
 
print(bola)
if  compra <=50000:
    print("no aplicas al dscuento") 
elif  bola ==1 and br :
    print(input( f"recibiste el descuento de $ {br}\n "))
elif bola ==2 and ba:
    print(input( f"recibiste el descuento de $ {ba}\n"))
elif bola ==3 and bam:
    print(input( f"recibiste el descuento de $ {bam}\n "))
elif bola ==4 and bbl:
    print(input(f"tu compra es gratis !felicitaciones¡ {bbl}\n "))       

else:
    print("los datos son incorrectos ")








