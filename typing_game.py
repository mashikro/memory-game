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
    timer = 5

    while timer > 0:
        time.sleep(1)
        timer = timer - 1
        
    print(chr(27) + "[2J")
    
        
intro()

number_life = 5

def level_1():
#displaying random word from word bank for 4 seconds and then clearing terminal 
    import random 
    print(random.choice(level_1_words))
    import time
    timer = 4
    while timer > 0:
        time.sleep(1)
        timer = timer - 1
    print(chr(27) + "[2J")
#getting user input
    level_1_input = input("Enter what you saw: >")
#evaluating user input
    if level_1_input == random.choice(level_1_words):
        print("You entered:", level_1_input)
        #move on to the next level
    #else: 
#if user messed up -- subtracting from their lives number_life = number_life -1
#if user has enough lives -- move on to the next level



level_1()