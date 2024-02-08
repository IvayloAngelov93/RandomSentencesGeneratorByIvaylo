from random import randint
list_of_names = ['Ivaylo', 'Roberto', 'Marian', 'Kiril']
list_of_places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
list_of_verbs = ["eats", "holds", "sees", "plays with", "brings"]
list_of_nouns = ["stones", "cake", "apple", "laptop", "bikes"]
list_of_adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
list_of_details = ["near the river", "at home", "in the park"]

def random_words(names, places, verbs, nouns, adverbs, details):
    random_name = names[randint(0, len(names)-1)]
    random_place = places[randint(0, len(places)-1)]
    random_verbs = verbs[randint(0, len(verbs)-1)]
    random_nouns = nouns[randint(0, len(nouns)-1)]
    random_adverbs = adverbs[randint(0, len(adverbs)-1)]
    random_details = details[randint(0, len(details)-1)]
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