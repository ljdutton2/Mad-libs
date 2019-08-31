# python3 madlibs.py
"""
algorithm:
first defining variables and then allowing for user input to create a storyline
"""


adjective = input("Type an adjective")
noun = input("Type a noun")
verb_past = input("Type a past tense verb")
adverb = input("Type an adverb")
adjective_2 = input("Type another adjective")
noun_2 = input("Type another noun")
noun_3 = input("Type another noun")
adjective_3 = input("Yype another adjective")
verb_2 = input("Type another verb")
adverb_2 = input("Type another adverb")
verb_past_2 = input("Type another past tense verb")
adjective_4 = input("Type one last adjective")

print("""Today I went to the zoo. I saw a {} {} jumping up and down in its tree.
 He {} {} through the large tunnel that led to its {} {} . I got some peanuts
  and passed them through the cage to a gigantic grey {} towering above my head.
   Feeding that animal made me hungry.I went to get a {} scoop of ice cream.
   It filled my stomach. Afterwards I had to {} {} to catch our bus.
    When I got home I {} my mom for a {} day at the zoo. """.format(adjective,
    noun, verb_past, adverb, adjective_2, noun_2, noun_3, adjective_3, verb_2,
    adverb_2, verb_past_2, adjective_4))
