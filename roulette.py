from random import randint

numer = randint(0, 14)

if 0 <= numer and numer <= 4:
    print("black" + str(numer))
elif 4 < numer and numer <= 9:
    print("red" + str(numer))
elif 9 < numer and numer <= 14:
    print("green" + str(numer))
