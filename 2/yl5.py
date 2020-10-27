suurus = float(input("Sisestage kirja suurus: "))
pealkiri = input("Sisestage kirja teema pealkiri: ")
fail = input("Kas kirjaga on kaasas fail? ")

if pealkiri == "":
    print("Kiri on spämm")
elif suurus > 1:
    if fail == "jah":
        print("Kiri on spämm")
    else:
        print("Kiri ei ole spämm")
else:
    print("Kiri ei ole spämm")