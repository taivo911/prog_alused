
from random import randint

poiss = int(input("Mitu poialpoissi tahab õunu: "))

i = 1
kulunud = 0
while (i<=poiss):
    ounu = randint(1, 2)
    print(str(ounu))
    kulunud += ounu
    i+=1

lumile = 14-kulunud
print("Lumivalgekesele jäi " + str(lumile) + " õuna.")