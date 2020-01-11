import random

level_1 = ["jazz", "fury", "keys", "bird", "cute", "pens", "blue", "leaf", "cake", "lady"] #4
level_2 = ["bliss", "brown", "corgi", "fazed", "grape", "green", "water", "couch", "glass", "laugh"] #5
level_3 = ["biotin", "bodega", "cherry", "deceit", "glazed", "flower", "pillow", "hamlet", "cheese", "kimono" ]  #6
level_4 = ["awkward", "balcony", "biofuel", "cripple", "duchess", "eyelash", "fireman", "ironman", "jukebox", "lovebug"] #7
level_5 = ["athletic", "bachelor", "collagen", "dedicate", "educated", "electron", "flawless", "haploids", "investor", "mocktail"] #8
level_6 = ["crocodile", "chocolate", "happiness", "pollution", "pineapple", "marijuana", "curiosity", "chemistry", "recycling", "magnesium"] #9
level_7 = ["watermelon", "creativity", "revolution", "rainforest", "adrenaline", "mozzarella", "medication", "temptation", "apothecary", "photogenic"] #10
level_8 = ["serendipity", "marshmallow", "imagination", "mathematics", "pomegranate", "promiscuous", "cytokinesis", "cauliflower", "chloroplast", "antioxidant"] #11
level_9 = ["trigonometry", "biodiversity", "hypothalamus", "supernatural", "aerodynamics", "immunization", "biochemistry", "carbohydrate", "tuberculosis", "cheeseburger"] #12
level_10 = ["schizophrenia", "mathematician", "mitochondrion", "parallelogram", "biotechnology", "metamorphosis", "hallucinogens", "hyperglycemia", "microorganism", "phytoplankton"] #13
level_11 = ["photosynthesis", "chromatography", "cardiovascular", "nanotechnology", "simplification", "flabbergasting", "automatization", "overprotective", "philanthropist", "hallucinogenic"] #14
level_12 = ["procrastination", "confidentiality", "crystallization", "experimentation", "hospitalization", "hemochromatosis", "decarboxylation", "neurobiological", "romanticization", "palaeontologist"] #15

all_levels = [level_1, level_2, level_3,level_4,level_5,level_6,level_7,level_8,level_9, level_10,level_11,level_12]

def random_word(level):
    '''Picks a random word from a set and returns it'''

    lst = all_levels[level]

    chosen_word = random.choice(lst)
    # l1_words.remove(chosen_word)

    return chosen_word

