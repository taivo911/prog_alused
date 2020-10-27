def kuu_nimi(jrk_nr):
    kuud = ['Jaanuar', 'Veebruar', 'Marts', 'Aprill', 'Mai', 'Juuni', 'Juuli', 'August', 'September', 'Oktoober', 'November', 'Detsember']
    kuu_nim = kuud[jrk_nr -1].lower()
    return kuu_nim

# F-n tagastab kp sonena
def kp_sonena(kp):
    eraldi = kp.split('.')
    kuu = kuu_nimi(int(eraldi[1]))
    return eraldi[0] + '. ' + kuu + ' ' + eraldi[2] + '. a'

# Sisend
kuupaev = input('Sisesta kuupaev kujul DD.MM.YYY: ')

# Valjund
print(kp_sonena(kuupaev))