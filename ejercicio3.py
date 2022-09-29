edad=int(input("ingresa tu edad en años \n"))
if 0<=edad<=4:
    print("el cliente ingresa gratis")
elif 4<=edad<18:
    print("el cliente debe pagar 20000")
elif 18<=edad<=60:
    print("el cliente debe pagar 15000")
elif edad>60:
    print("el cliente solo debe pagar 3000")
else:
    print("no cumple con el criterio")