from random import randint

valik = input('Kas soovite istekohta ise valida ("ise") või loosida("loos")? ')
loositud = randint(1, 3)
if loositud == "1" or loositud == "2":
    loositud = "Istekoht ei ole akna ääres."
else:
    loositud = "Aknakoht."

if valik == "ise":
    valik2 = input('Kas soovite istuda akna ääres("aken") või mitte ("muu")? ')
    if valik2 == "aken":
        print("Valisite ise. Aknakoht.")
    else:
        print("Valisite ise. Istekoht ei ole akna ääres. ")
else:

    print("Istekoht loositi. " + loositud)