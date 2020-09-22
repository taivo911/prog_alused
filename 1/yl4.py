nimi = input("Sisestage oma nimi:")
lubatud = input("Sisestage lubatud kiirus (km/h):")
tegelik = input("Sisestage tegelik kiirus (km/h):")
vastus = str(min(190,(int(tegelik) - int(lubatud))* 3))

print(nimi +", kiiruse ületamise eest on Teie trahv " + vastus + " eurot.")
