import time
import random 

#12 levels thus 12 word banks. Note: each level gets longer by 1 character to make each ascending level more challenging. 
level_1_words = ["jazz", "fury", "keys", "bird", "cute", "pens", "blue", "leaf", "cake", "lady"] #4
level_2_words = ["bliss", "brown", "corgi", "fazed", "grape", "green", "water", "couch", "glass", "laugh"] #5
level_3_words = ["biotin", "bodega", "cherry", "deceit", "glazed", "flower", "pillow", "hamlet", "cheese", "kimono" ]  #6
level_4_words = ["awkward", "balcony", "biofuel", "cripple", "duchess", "eyelash", "fireman", "ironman", "jukebox", "lovebug"] #7
level_5_words = ["athletic", "bachelor", "collagen", "dedicate", "educated", "electron", "flawless", "haploids", "investor", "mocktail"] #8
level_6_words = ["crocodile", "chocolate", "happiness", "pollution", "pineapple", "marijuana", "curiosity", "chemistry", "recycling", "magnesium"] #9
level_7_words = ["watermelon", "creativity", "revolution", "rainforest", "adrenaline", "mozzarella", "medication", "temptation", "apothecary", "photogenic"] #10
level_8_words = ["serendipity", "marshmallow", "imagination", "mathematics", "pomegranate", "promiscuous", "cytokinesis", "cauliflower", "chloroplast", "antioxidant"] #11
level_9_words = ["trigonometry", "biodiversity", "hypothalamus", "supernatural", "aerodynamics", "immunization", "biochemistry", "carbohydrate", "tuberculosis", "cheeseburger"] #12
level_10_words = ["schizophrenia", "mathematician", "mitochondrion", "parallelogram", "biotechnology", "metamorphosis", "hallucinogens", "hyperglycemia", "microorganism", "phytoplankton"] #13
level_11_words = ["photosynthesis", "chromatography", "cardiovascular", "nanotechnology", "simplification", "flabbergasting", "automatization", "overprotective", "philanthropist", "hallucinogenic"] #14
level_12_words = ["procrastination", "confidentiality", "crystallization", "experimentation", "hospitalization", "hemochromatosis", "decarboxylation", "neurobiological", "romanticization", "palaeontologist"] #15


all_level_words = [level_1_words, level_2_words, level_3_words, level_4_words, level_5_words, level_6_words, level_7_words, level_8_words, level_9_words, level_10_words, level_11_words, level_12_words]

def clear_terminal():
    """clears terminal"""
    print(chr(27) + "[2J")

def intro():
    """greets user and gives instructions"""
    print()
    print("Hi there! Welcome to my typing/memory game.")
    print("🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠 🧠")
    print("Its purpose is to help you work on your muscle memory and improve your typing accuracy and speed 🤓.")
    print()
    print("Instructions:")
    print("*************")
    print("The game will flash you a word for --3 seconds-- and then it will disappear.")
    print("Your task is to type the word you saw as fast and as accurately as possible.") 
    print()
    print("🥇 🥇 How to win🥇 🥇")
    print("*************")
    print("If you meet the (1)typing speed & (2)accuracy criteria you will move on to the next level.")
    print("Typing speed: 5 seconds")
    print("Typing accuracy: all characters must match displayed word")
    print()
    print("*************")
    print("If you don't meet the requirements....👿 👿 👿")
    print("You are given 5 lives for the entire game. If you loose all 5 lives....GAME OVER!!")
    print()
    print("                 *************************************** ")

    #clear intro
    input("Press Enter to continue ▶️ ...")
    clear_terminal()

def test_word(chosen_word):
    """Shows word, gets input from user and calculates elapsed time."""

    print(chosen_word)
    #displays for 3 seconds
    time.sleep(3)
    clear_terminal()
    start_time = time.time()
    #getting user input
    test_input = input("Enter what you saw: >")
    test_input = test_input.lower()
    end_time = time.time()
    #calculate elapsed time
    elapsed_time = end_time - start_time
    return (test_input, elapsed_time) #this is a tuple

number_life = 5

def play_level(level_words):
    """Uses helper functions to determine if player can move on to next level. 
    Determines how many lives a player has left"""
    global number_life 
    
    while number_life > 0:
        print()
        print("Remmember this word: ")
        print()
        chosen_word = random.choice(level_words)
        level_words.remove(chosen_word)  #removes printed word from lst to avoid repitition. 
        (test_input, elapsed_time) = test_word(chosen_word) #the return of test_word() is a tuple

        if test_input == chosen_word and elapsed_time <= 5:
            print("Success 👏")
            print()
            print("***** User Stats *****")
            print("Typing speed:", elapsed_time, "seconds")
            print("Typing accuracy: Perfect match -->", test_input)
            print("Lives remaining: ", number_life)
            print("=========================================")
            input("Press Enter to continue to the next level ▶️ ...")
            clear_terminal()
            return True

        else:
            number_life = number_life - 1 
            print()
            if number_life > 0:
                print("👎 Try again👎")
    return False



def play_game():
    for idx, level_words in enumerate(all_level_words):
        print("Level", [idx+1])
        play_level(level_words)
    if number_life > 0:
        print("🥇 🥇YOU WIN! 🥇 🥇")
    else:
        print("👿 Game over! 👿")
    
def main():  
    intro()  
    play_game()    

main()