def banner(message):
    message = message.upper()
    return message

kordi = int(input('Mitu korda soovite reklaamlauset kuvada? '))
lause = input('Millist reklaamlauset soovite? ')

while kordi > 0:
    print(banner(lause))
    kordi -= 1
