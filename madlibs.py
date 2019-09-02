# python3 madlibs.py

#TITLE
name = input("What is your name?")
def get_title(name):
    print ("Hello" + name)
    print ("Welcome to A day at the zoo Mad Libs")

get_title(name)




user_input=input()
adjective = input("Type an adjective")
noun = input("Type a noun")
verb_past = input("Type a past tense verb")
adverb = input("Type an adverb")
adjective_2 = input("Type another adjective")
noun_2 = input("Type another noun")
noun_3 = input("Type another noun")
adjective_3 = input("Type another adjective")
verb_2 = input("Type another verb")
adverb_2 = input("Type another adverb")
verb_past_2 = input("Type another past tense verb")
adjective_4 = input("Type one last adjective")

words = [adjective,noun,verb_past,adverb,adjective_2,noun_2,noun_3,adjective_3,verb_2,adverb_2,verb_past_2,adjective_4]


print("""Today I went to the zoo. I saw a {} {} jumping up and down in its tree.
 He {} {} through the large tunnel that led to its {} {} . I got some peanuts
  and passed them through the cage to a gigantic grey {} towering above my head.
   Feeding that animal made me hungry.I went to get a {} scoop of ice cream.
   It filled my stomach. Afterwards I had to {} {} to catch our bus.
    When I got home I {} my mom for a {} day at the zoo. """.format(words[0],
    words[1], words[2], words[3], words[4], words[5], words[6], words[7], words[8],
    words[9], words[10], words[11]))



#Madlibs story found https://www.woojr.com/summer-mad-libs/zoo-mad-libs/
