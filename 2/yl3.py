print('Sisesta vanus t2isarvuna')
v = int(input())

print('Sisesta sugu (M/N)')
s = str.lower(input())

print('Sisesta treeningu tüüp (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening)')
t = int(input())
if (s == 'm'):
    pulssMin= (220 - v)
    pulssMax= (220 - v)
elif  (s == 'n'):
    pulssMin = (206 - v * .88)
    pulssMax = (206 - v * .88)
if (t == 1):
    pulssMin *= .5
    pulssMax *= .7
elif (t == 2):
    pulssMin *= .7
    pulssMax *= .8
elif (t == 3):
    pulssMin *= .8
    pulssMax *= .87
print('Pulsisagedus peaks olema vahemikus ' +str(round(pulssMin))+ ' kuni ' + str(round(pulssMax)))