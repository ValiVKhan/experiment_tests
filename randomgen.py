import random


##MY RANDOM NUMBER GENERATOR##

count = int(input("Count? "))

number_lenght = int(input("Length? "))

global run
run = 0
while 1:
    if run == count:
        break
    else:
        if number_lenght == 1:
            print((random.SystemRandom().randint(1, 9)))
        if number_lenght == 2:
            print((random.SystemRandom().randint(10, 99)))
        if number_lenght == 3:
            print((random.SystemRandom().randint(100, 999)))
        if number_lenght == 4:
            print((random.SystemRandom().randint(1000, 9999)))
        if number_lenght == 5:
            print((random.SystemRandom().randint(10000, 99999)))
        if number_lenght == 6:
            print((random.SystemRandom().randint(100000, 999999)))
        if number_lenght == 7:
            print((random.SystemRandom().randint(1000000, 9999999)))
        if number_lenght == 8:
            print((random.SystemRandom().randint(10000000, 99999999)))
        if number_lenght == 9:
            print((random.SystemRandom().randint(100000000, 999999999)))
        if number_lenght == 10:
            print((random.SystemRandom().randint(1000000000, 9999999999)))
        if number_lenght == 11:
            print((random.SystemRandom().randint(10000000000, 99999999999)))
    run = run + 1
