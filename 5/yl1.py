fail =  open("arvud1.txt", encoding = "UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()

aasta = int(input("Sisesta aasta (2011-2019): "))
algus=[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

indeks = algus.index(aasta)
inimesi = vastuvõetud[indeks]

print("Aastal " + str(aasta) + " oli " + str(inimesi) + " vastu võetud üliõpilast.")