# piedra papel tijera 

from random import randint


compu=randint(1,3)
   
usu= int(input("digite 1 = piedra 2= papel 3= tigera \n" )) 
print (compu, "el compu eligio ")


if compu == usu:
    print(" empate ")
elif compu ==1 and usu ==3 or compu ==2 and usu ==1 or compu ==3 and usu==2:
    print("gana el compu")
elif usu ==1 and compu ==3 or usu ==2 and compu ==1 or usu ==3 and compu ==2:
    print(" !felicitaciones¡ ganaste ") 
else:
    print ("revise su seleccion ")
