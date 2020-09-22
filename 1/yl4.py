nimi = input("Sisestage oma nimi:")
lubatud = input("Sisestage lubatud kiirus (km/h):")
tegelik = input("Sisestage teglik kiirus (km/h):")
vastus = (int(tegelik) - int(lubatud))* 3
trahv = str(min(190,vastus))

print(nimi +",kiiruse ületamise eest on teie trahv " + trahv + " eurot.")
