import random

l1_words = ["jazz", "fury", "keys", "bird", "cute", "pens", "blue", "leaf", "cake", "lady"] #4
l2_words = ["bliss", "brown", "corgi", "fazed", "grape", "green", "water", "couch", "glass", "laugh"] #5
# level_3_words = ["biotin", "bodega", "cherry", "deceit", "glazed", "flower", "pillow", "hamlet", "cheese", "kimono" ]  #6
# level_4_words = ["awkward", "balcony", "biofuel", "cripple", "duchess", "eyelash", "fireman", "ironman", "jukebox", "lovebug"] #7
# level_5_words = ["athletic", "bachelor", "collagen", "dedicate", "educated", "electron", "flawless", "haploids", "investor", "mocktail"] #8
# level_6_words = ["crocodile", "chocolate", "happiness", "pollution", "pineapple", "marijuana", "curiosity", "chemistry", "recycling", "magnesium"] #9
# level_7_words = ["watermelon", "creativity", "revolution", "rainforest", "adrenaline", "mozzarella", "medication", "temptation", "apothecary", "photogenic"] #10
# level_8_words = ["serendipity", "marshmallow", "imagination", "mathematics", "pomegranate", "promiscuous", "cytokinesis", "cauliflower", "chloroplast", "antioxidant"] #11
# level_9_words = ["trigonometry", "biodiversity", "hypothalamus", "supernatural", "aerodynamics", "immunization", "biochemistry", "carbohydrate", "tuberculosis", "cheeseburger"] #12
# level_10_words = ["schizophrenia", "mathematician", "mitochondrion", "parallelogram", "biotechnology", "metamorphosis", "hallucinogens", "hyperglycemia", "microorganism", "phytoplankton"] #13
# level_11_words = ["photosynthesis", "chromatography", "cardiovascular", "nanotechnology", "simplification", "flabbergasting", "automatization", "overprotective", "philanthropist", "hallucinogenic"] #14
# level_12_words = ["procrastination", "confidentiality", "crystallization", "experimentation", "hospitalization", "hemochromatosis", "decarboxylation", "neurobiological", "romanticization", "palaeontologist"] #15

# all_levels = [l1_words, l2_words]

def random_word():
    '''Picks a random word from a set and returns it'''

    chosen_word = random.choice(l1_words)

    return chosen_word

