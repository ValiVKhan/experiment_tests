
linenum = 0

def finder():
    file_open = open('key.txt', 'r')
    all_lines = file_open.readlines()

    str = (all_lines[linenum])

    file_open.close()

    (str.find("is the best"))

    str2 =  (str.find("is the best" or "is the correct") - 2)
    str3 = (str.find("correct answer is") + 19)

    if str2 != -3:
        file = open('key.txt', 'r') 
        f = open("answer.txt", "a")
        f.write(((str[str2])))
        f.write("\n")
        f.close()
    if str3 != 18:
        file = open('key.txt', 'r') 
        f = open("answer.txt", "a")
        f.write(((str[str3])))
        f.write("\n")
        f.close()



while linenum < 1843:  
    finder()
    linenum = linenum + 1

print("Mission Complete")




