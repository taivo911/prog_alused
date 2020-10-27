ring = int(input("Sisesta ringide arv: "))

ringi_nr = 1
porgand = 0

while (ringi_nr <= ring):
    print(str(ringi_nr) + ".ring")
    if(ringi_nr % 2==0):
        print("said " + str(ringi_nr) + " porgandit")
        porgand = porgand + ringi_nr
        print("Porgandite koguarv on " + str(porgand))
    ringi_nr +=1