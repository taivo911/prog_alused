ainepunkt = input("Sisesta ainepunktide arv:")
nadal = input("Sisesta nädalate arv:")
ajakulu = int(26)
vastus = str((int(ainepunkt) * int(ajakulu)) / int(nadal))

print("Teie eeldatav ajakulu on " + vastus + " tundi.")