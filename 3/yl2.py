
ringide_arv = int(input("Sisestage ringide arv: "))

ringi_number = 1 # alustame jooksu 1. ringist

porgandite_arv = 0

while(ringi_number <= ringide_arv):
    print(str(ringi_number) + ". ring")  #protsessi kontrollida saab printides ringi_number, kuvab 7 tk
    #suurendame muutuja v22rtust ringi l2bimisel
    if(ringi_number % 2 == 0):
        print("Said " + str(ringi_number) + " porgandit.")
        porgandite_arv = porgandite_arv + ringi_number
        print("Hetkel on kokku " + str(porgandite_arv) + " porgandit.")
    ringi_number += 1

print("Porgandite koguarv on " + str(porgandite_arv))
