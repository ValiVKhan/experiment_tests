import speech_recognition as sr
from hanger import hanger
from time import sleep
import random


name_number = (random.SystemRandom().randint(0, 211))
file_open = open('words.txt', 'r')

all_lines = file_open.readlines()

random_name = (all_lines[name_number])
word = random_name
print(word)
wordlength = (len(word))

wordarray = ["_"]*(wordlength - 1)

global hangershow
hangershow = 0
used=[]
def asker():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source) or input("what letter?")
        try:
            text = r.recognize_google(audio)
            letter = (format(text))
            if letter.__contains__("letter"):
                global guess
                guess = (letter[7]).lower()
                if guess not in used:
                    print(guess)
                    print("\n")
                    used.append(guess)
                    print (' ' .join(used))
                else:
                    print("letter already been used before!")
                    asker()
            else:
                asker()
        except:
            print("\n")


def searcher():
    letter =  0
    global guess
    global wrongincount
    wrongincount = 0
    while letter < wordlength:
        if guess == (word[letter]):
            wordarray[letter] = guess
            letter +=1
        else:
            letter+=1
            wrongincount +=1
            continue
    if wrongincount == wordlength:
        global hangershow
        hangershow +=1
        print(hanger[hangershow])
    print ('' .join(wordarray))


asker()
searcher()
global combined
combined = ('' .join(wordarray))

while 1:
    if combined == word:
        print(hanger[7])
        break
    elif hangershow < 6:  
        asker()
        searcher()
    if hangershow == 6:
        print(word)
        break    