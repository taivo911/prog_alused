#print('Sisesta ees- ja perekonnanimi:')
#nimi = str(input()).title()
#print(nimi)

nimi = input("Sisest ees ja perekonnanimi: ")
for osanimest in nimi.split(" "):
    print(osanimest.capitalize(), end=" ")