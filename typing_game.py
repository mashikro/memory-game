#print("Hello world!")
import time
import random 

#create word banks for each level. Each ascending level's word len will be +1char 
level_1_words = ["jazz", "fury", "keys", "bird", "cute", "pens", "blue"]

def intro():
    print("Hi there! Welcome to my typing/memory game.")
    print("🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠")
    print("Its purpose is to help you work onn your muscle memory and improve your typing accuracy and speed 🤓.")
    print("*************")
    print("Instructions: ")
    print("*************")
    print("The game will flash you a word for X seconds and then it will disappear. Your task is to type the word you saw as fast and as accurately as possible.") 
    print("*************")
    print("If you meet the typing speed and accuracy criteria you will move on to the next level.")
    print("Typing speed: XX")
    print("Typing accuracy: XX")
    print("*************")
    print("If you don't meet the requirements....👿 👿 👿")
    print("You are given 5 lives for the entire game. If you loose all 5 lives....GAME OVER!!")
    print("*************")

    #clear intro
    time.sleep(5)
    print(chr(27) + "[2J")
         
intro()


#number_life = 5
#while number_life > 0:
    

def level_1():
    number_life = 5
    #displaying random word from word bank
    print(random.choice(level_1_words))
    #displays for 4 seconds
    time.sleep(4)
    #clearing terminal
    print(chr(27) + "[2J")
    #getting user input
    time.time()
    x = time.time()
    level_1_input = input("Enter what you saw: >")
    #calculate elapsed time
    y = time.time()
    elapsed_time = y - x 
    #evaluating user input
    if level_1_input == random.choice(level_1_words):
        if elapsed_time <= 5:
            print("You entered:", level_1_input)
        #move on to the next level
    else:
        print("Try again")
        number_life = number_life - 1
            
    #if user messed up -- subtracting from their lives number_life = number_life -1
    #if user has enough lives -- move on to the next level

level_1()