from time import sleep

f = open("typer.txt","r")
all_lines_variable = f.readlines()

fo = open("ans.txt","w")

linenum = 1

def replacer():
    
    line = (all_lines_variable[linenum - 1])

    word = line.find("a"or"e"or"i"or"u"or"o")

    if word != -1:
        fo.write(line)


x = 100
while linenum != 4565:
    replacer()
    linenum += 1
    if linenum == x:
        print (linenum)
        x = x + 100
