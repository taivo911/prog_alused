
inimesed = 50
bussiKohad = 35

mahaJaab = inimesed % bussiKohad
bussid = (inimesed - mahaJaab) / bussiKohad
bussiInimesed = inimesed - mahaJaab
print('Transportida on vaja ' + str(inimesed) + ' inimest.')
print('Uhes bussis on: ' +str(bussiKohad) + ' kohta.')
print('Tellida on vaja ' + str(bussid) + ' bussi.')
print('Bussidesse mahub ' + str(bussiInimesed) + ' inimest.')
print('Maha jaab ' + str(mahaJaab) + ' inimest.')