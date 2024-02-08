from random import choice
list_of_names = ['Ivaylo', 'Roberto', 'Marian', 'Kiril', "Peter"]
list_of_places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Pernik"]
list_of_verbs = ["eats", "holds", "sees", "plays with", "brings"]
list_of_nouns = ["stones", "cake", "apple", "laptop", "bikes", "iron",]
list_of_adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly", "hot"]
list_of_details = ["near the river", "at home", "in the park", "at the office", "in the gym", "on the plane"]

def random_words(names, places, verbs, nouns, adverbs, details):
    random_name = choice(names)
    random_place = choice(places)
    random_verbs = choice(verbs)
    random_nouns = choice(nouns)
    random_adverbs = choice(adverbs)
    random_details = choice(details)
    return random_name, random_place, random_verbs, random_nouns, random_adverbs, random_details

name, place, verb, noun, adverb, detail = random_words(names=list_of_names,
                                                       places=list_of_places,
                                                       verbs=list_of_verbs,
                                                       nouns=list_of_nouns,
                                                       adverbs=list_of_adverbs,
                                                       details=list_of_details)

def get_text():
    text = f"""
    Hello, my name is {name}.
    I am born in the most beautiful city {place}? 
    I really like to {verb} {noun} {adverb} {detail} to the river!
    """
    return text

print(get_text())