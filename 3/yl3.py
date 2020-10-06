from random import randint

print('Täringute arv')
taringud = int(input())
while taringud > 0:
    print(randint(1, 6))
    taringud-=1