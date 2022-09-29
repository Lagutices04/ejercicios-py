from random import randint
from xml.dom.expatbuilder import ElementInfo
dado1=randint(1,6)
 
dado2=randint(1,6)
 
 
total2=dado1+dado2
total3=dado1+dado2
 
 
if dado1== 1 and dado2==1:
    print("si sale un par de unos en los dados,ganaste")
 
elif dado1==2 and dado2==1 :
    print(f"si es {total2}  en los dados ganaste")
 
elif dado1==6 and dado2==5:
    print(f"si es {total3} en los dados ganaste")
 
elif dado1==2 or dado2==12:
    print("si se obtiene 2 o 12 en los dados ganaste ")
 
elif dado1==5 and dado2==2:
    print(f"si es {total3}  en los dados ganaste")
else:
    ("perdiste")
