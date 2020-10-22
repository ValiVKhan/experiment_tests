from time import sleep
import random

hanger=['''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
      ~Loser~  /|\    |  ~Loser~ 
                |     |
               / \   _|_''','''
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    
                
                    \O/      
          ~WINNER~   |   ~WINNER~        
                     |    
                    / \ 
                                       
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']

#Variable assign
#Wrong is what contorls the graphics
global wrong
wrong = -1

#The word being found
name_number = (random.SystemRandom().randint(0, 212))
file_open = open('wrds.txt', 'r')

all_lines = file_open.readlines()

random_name = (all_lines[name_number])
word = random_name
print(word)
#Loser count controls the break out of the loop is the player never guesses correctly and loses
global losercount
losercount = 0
#Asking for a letter, this is in function becasue it is used repetitvley

def asker():
    global guess
    guess =  (input("What is your letter guess? "))


#The lenght of the world, later used to see the amount of blanks
global wordlenth
wordlenth = (len(word))

#The amount of blanks needed
global blank
wordwrite = wordlenth - 1
blank = ["_"]*wordwrite
global calc
calc = 1
# Finder runs through each character of the word and searches for the guess letter that was inputted.
def finder():
    Letter_list.append(guess)
    #Letter is used when searching through the word
    letter = 0
    #Wroner is a counter which is only counted for when the guess letter is not found in a postion of the word
    wroner = 0
    while letter < wordlenth:
        if guess == (word[letter]):
            #print(word[letter])
            #print (letter)
            blank[letter] = guess
            #print(blank)
            letter = letter + 1
            global calc
            calc = calc + 1
        else:
            letter = letter + 1
            wroner = wroner + 1
            global losercount
            losercount = losercount + 1
    if wroner == wordlenth:
        global wrong
        wrong = wrong + 1
        #wrong counts what graphic to display from the array hanger
        if wrong != 7:
            print(hanger[wrong])
    #converts array to a string
    print ('' .join(blank))
    global blanks
    blanks = (''.join(blank))

#asker and finder are the  fucntions and must be ran before once because they give calues for the loop
Letter_list = []
asker()
finder()
#The while loop controlling everything
while 1:
    #If the blanks dont equal the word ask for another letter and run finder
    if blanks != word:
        asker()
        if guess in Letter_list:
            print("Letter has already been used before!")
        else:
            finder()
        #If los
    if wrong == 6:
        print(word)
        break
    if calc == wordlenth:
        #Prints winner when the blank and word match
        print(hanger[7])
        break



    

