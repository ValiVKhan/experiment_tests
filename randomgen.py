import random


##MY RANDOM NUMBER GENERATOR##

count = int(input("Count? "))

number_lenght = int(input("Length? "))

global run
run = 0
global f
f = open("random.txt", "w")
while 1:
    if run == count:
        break
    else:
        if number_lenght == 1:
            f.write((str(random.SystemRandom().randint(1, 9))))
            f.write("\n")
        if number_lenght == 2:
            f.write((str(random.SystemRandom().randint(10, 99))))
            f.write("\n")
        if number_lenght == 3:
            f.write((str(random.SystemRandom().randint(100, 999))))
            f.write("\n")
        if number_lenght == 4:
            f.write((str(random.SystemRandom().randint(1000, 9999))))
            f.write("\n")
        if number_lenght == 5:
            f.write((str(random.SystemRandom().randint(10000, 99999))))
            f.write("\n")
        if number_lenght == 6:
            f.write((str(random.SystemRandom().randint(100000, 999999))))
            f.write("\n")
        if number_lenght == 7:
            f.write((str(random.SystemRandom().randint(1000000, 9999999))))
            f.write("\n")
        if number_lenght == 8:
            f.write((str(random.SystemRandom().randint(10000000, 99999999))))
            f.write("\n")
        if number_lenght == 9:
            f.write((str(random.SystemRandom().randint(100000000, 999999999))))
            f.write("\n")
        if number_lenght == 10:
            f.write((str(random.SystemRandom().randint(1000000000, 9999999999))))
            f.write("\n")
        if number_lenght == 11:
            f.write((str(random.SystemRandom().randint(10000000000, 99999999999))))
            f.write("\n")
    run = run + 1
    
    
