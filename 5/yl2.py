fail =  open("arvud2.txt", encoding = "UTF-8")
tehing = []
for rida in fail:
     tehing.append(float(rida))
fail.close()

for el in tehing:
    if el > 0:
        print(str(el))
    else:
        continue