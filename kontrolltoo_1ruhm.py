# Impordime fandom funktsiooni, et see toimiks.
from random import randint
# Funktsiooni loomine, et teada saada, kui palju inimesi erinevate võistluste korral osaleb.
def inimeste_arv(naiskondi, tugiisikuid):
    inimesi_kokku = naiskondi*(22+tugiisikuid)
    return inimesi_kokku

turniiridel_osalenud_naiskondade_arvud = [12, 12, 16, 16, 16, 16, 24]

# Küsime kasutajalt toimumise asukoha ja väljastame selle ekraanile.
asukoht = input("Kus toimusid maailmameistrivõistulsed? ")
print("Turniir toimus askukohas " + asukoht + ".")

# Küsime kasutajalt, et mitu turniiri toimus
turniiride_koguarv = int(input("Kui palju turniire toimus? "))

# Genereerime naistkondade arvu juhuarvuna vahemikus 10-30
naiskondade_arv = 0
arv = []
i = 1
kulunud = 0
while (i<=turniiride_koguarv):
    arv.append(randint(10, 30))
    i+=1

# Defineerime koguväärtuse elemendi.
kokku = 0

# Tekitatud juhuslikust järjendist lisame naiskondade koguse.
for el in arv:
    if el < 15:
         # Kui turniiril on vähem kui 15 võistkonda, siis on iga võistkonna tugiisikute arv 10
        tugiisikuid = 10
        print("Turniiril oli " + str(el) + " naiskonda ja vastavalt sellele inimesi: " + str(inimeste_arv(el, tugiisikuid))+ " inimest.")
        kokku = kokku + inimeste_arv(el, tugiisikuid)
    else:
        # Kui turniiril on 8 võistkonda, siis on iga võistkonna tugiisikute arv 8
        tugiisikuid = 8
        print("Turniiril oli " + str(el) + " naiskonda ja vastavalt sellele inimesi: " + str(inimeste_arv(el, tugiisikuid)) + " inimest.")
        kokku = kokku + inimeste_arv(el, tugiisikuid)

# Väljastame turniiridel osalenud inimeste koguarvu
print("Turniiridel osales kokku " + str(kokku) + " inimest.")
