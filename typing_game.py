import time
import random 

level_1_words = ["jazz", "fury", "keys", "bird", "cute", "pens", "blue"]
#level_2_words = ["bliss", "brown", "corgi", "fazed", "grape"]

def clear_terminal():
    print(chr(27) + "[2J")

def intro():
    print("Hi there! Welcome to my typing/memory game.")
    print("🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠")
    print("Its purpose is to help you work on your muscle memory and improve your typing accuracy and speed 🤓.")
    print("*************")
    print("Instructions: ")
    print("*************")
    print("The game will flash you a word for --4 seconds-- and then it will disappear. Your task is to type the word you saw as fast and as accurately as possible.") 
    print("*************")
    print("If you meet the typing speed and accuracy criteria you will move on to the next level.")
    print("Typing speed: 5 seconds")
    print("Typing accuracy: all characters must match displayed word")
    print("*************")
    print("If you don't meet the requirements....👿 👿 👿")
    print("You are given 5 lives for the entire game. If you loose all 5 lives....GAME OVER!!")
    print("*************")

    #clear intro
    time.sleep(5)
    clear_terminal()

def test_word(chosen_word):
    """Shows word, gets input from user. Calculates elapsed time."""
    print(chosen_word)
    #displays for 4 seconds
    time.sleep(2)
    clear_terminal()
    #getting user input
    x = time.time()
    test_input = input("Enter what you saw: >")
    #calculate elapsed time
    y = time.time()
    elapsed_time = y - x
    return (test_input, elapsed_time)
   

## returns True if they succeeded, otherwise false when game over.
def level_1():
    """level 1: Uses helper functions to determine if player can move on to next level"""
    number_life = 5

    while number_life > 0:
        print("Lives remaining: ", number_life)
        print("Remmember this word: ")
        chosen_word = random.choice(level_1_words)
        result = test_word(chosen_word)
        test_input = result[0]
        elapsed_time = result[1]

        if test_input == chosen_word and elapsed_time <= 5:
            print("Level 1 - Success 👏")
            print("***** User Stats *****")
            print("Typing speed:", elapsed_time, "seconds")
            print("Typing accuracy: Perfect match -->", test_input)
            print("LEVEL 2")
            return True

        else:
            return False

def main():  
    intro()
    level_1()       
    print(test_word(random.choice(level_1_words)))

main()