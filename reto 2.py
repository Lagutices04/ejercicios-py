#adivina el numero
print("piensa en un numero")
print("a ese resultado sumale 5 \n a ese resultado multiplicale 3 \n a ese resultado restale 15  ")
res=int(input("ingresa el resultado"))
num=res/3
print(f"el numero que pensaste es {int(num)}")
resp=input("el resultado es correcto, digite si o no \n")
if resp=="si" or resp=="SI" or resp=="Si" or resp=="sI":
    print("soy todo un adivino")
else:
    print("rectifica las cuentas te daras cuenta que nunca me equivoco")
