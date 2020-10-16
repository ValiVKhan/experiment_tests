
linenum = 0

def finder():
    file_open = open('key.txt', 'r')
    all_lines = file_open.readlines()

    str = (all_lines[linenum])

    file_open.close()

    
    str2 =  (str.find("is the best answer" or "is correct."))
    backspace = 2
    if str2 != -1:
        while 1:
            if (str[str2-backspace]) == " ":
                break
            else:
                backspace = backspace + 1
        
        answerlength = backspace - 2
        printer = 0
        answerstart = (str2 - 2 - answerlength)
        while printer <= answerlength:
            file = open('key.txt', 'r') 
            f = open("answer.txt", "a")
            f.write(str[answerstart + printer])
            printer =  printer + 1
        f.write("\n")
        f.close()

while linenum < 1843:  
    finder()
    linenum = linenum + 1


print("Mission Complete")




