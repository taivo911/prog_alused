fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()
#print(vastuvõetud[1:])

print('Sisesta aasta, et leida sisseastujate arv: ')
a = int(input()) - 2011 #lahutame soovitud aastast, et võrdsustada ridade arvuga
for i in range(9):
     if i == a:
          print('Vastu võeti ' + str(vastuvõetud[i]) + " õpilast.")
print("Ilusat päeva jätku!")