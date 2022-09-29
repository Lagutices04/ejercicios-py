leche=input("¿trajo la leche? \n digite s o n \n")
pan=input("¿trajo el pan? \n digite s o n \n")
huevos=input("trajo los huevos \n digite s o n \n")
 
#mama brava
if leche=="s" and pan=="s" and huevos=="s":
    print("listo,venga a desayunar")
else:
    print("coscorron")
#mama plena
if leche=="s" or pan=="s" or huevos=="s":
    print("dale rey")
else:
    print("me toco ir a mi ")