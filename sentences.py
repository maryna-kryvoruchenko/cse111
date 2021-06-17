import random  

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    else:
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb 

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)

    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = preposition + " " +  determiner + " " + noun 
    
    return prepositional_phrase

def make_game():
    intro_q = input("Would you like to create your own sentence?(yes/no) ")
    if intro_q.lower() == "yes":
        quantity_q = input("Singular or Plural?(s/p) ")
        tense_q = input("Past, present, or future? ")
        if quantity_q.lower() == "s" and tense_q.lower == "past":
            sentence = print(f"{get_determiner(1)} {get_noun(1)} {get_verb(1, 'past')} {get_prepositional_phrase(1)}")
        elif quantity_q.lower() == "s" and tense_q.lower == "present":
            sentence = print(f"{get_determiner(1)} {get_noun(1)} {get_verb(1, 'present')} {get_prepositional_phrase(1)}")
        elif quantity_q.lower() == "s" and tense_q.lower() == "future":
            sentence = print(f"{get_determiner(1)} {get_noun(1)} {get_verb(1, '')} {get_prepositional_phrase(1)}")
        elif quantity_q.lower() == "p" and tense_q.lower() == "past":
            sentence = print(f"{get_determiner(0)} {get_noun(0)} {get_verb(0, 'past')} {get_prepositional_phrase(0)}")
        elif quantity_q.lower() == "p" and tense_q.lower() == "present":
            sentence = print(f"{get_determiner(0)} {get_noun(0)} {get_verb(0, 'present')} {get_prepositional_phrase(0)}")
        else:
           sentence = print(f"{get_determiner(0)} {get_noun(0)} {get_verb(0, '')} {get_prepositional_phrase(0)}")
    else:
        sentence = print("Thank you for participation")
    return sentence

def main():
    # 1 
    article = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "past")
    
    print(f"1. {article} {noun} {verb} {get_prepositional_phrase(1)}") 
    print() 

    #2 
    article = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "past")

    print(f"2. {article} {noun} {verb} {get_prepositional_phrase(0)}")
    print() 

    # 3

    article = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "present")

    print(f"3. {article} {noun} {verb} {get_prepositional_phrase(1)}")
    print() 

    # 4

    article = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "present")

    print(f"4. {article} {noun} {verb} {get_prepositional_phrase(0)}")
    print() 
    
    # 5
    print(f"5. {get_determiner(1)} {get_noun(1)} {get_verb(1, '')} {get_prepositional_phrase(1)}")
    print() 

    #6 
    article = get_determiner(0)
    noun = get_noun(0)
    verb = get_verb(0, "")

    print(f"6. {article} {noun} {verb} {get_prepositional_phrase(0)}")
    print() 

    make_game()
    
main()