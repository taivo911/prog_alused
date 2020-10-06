print('Sisesta perekonnanimi: ')
n = str(input())
if (n[-2:] == 'ne'):
    print('Abielus')
elif (n[-2:] == 'te'):
    print('Vallaline')
elif (n[-1] == 'e'):
    print('Määramata')
else:
    print('Pole leedulanna perekonnanimi')