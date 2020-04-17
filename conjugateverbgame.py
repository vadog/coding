import os
import random

import verbOrganizer


chooseDirectory = input("choose directory: ")


fileName = chooseDirectory
propernoun = ["yo","tu","usted","nosotros","ustedes"]
round = 0
points= 0
rounds = 2

print("Answer these spanish questions, each time you get one wrong you loose 1 point, if you get both the questions right you get 3 points.")



#prints amount of verbs
print ("there are",len(verbOrganizer.build(fileName)),"verbs")

while round < rounds:

    randomFile = random.randrange(0,len(verbOrganizer.build(fileName)))
    eglishVerb = verbOrganizer.build(fileName)[randomFile][1]
    spanishVerb =  verbOrganizer.build(fileName)[randomFile][0]
    randomPropernoun = random.randrange(0,4)
    
    # Question about present tense
    print ("Complete the sentence using "+eglishVerb+ ": ",propernoun[randomPropernoun],)
    answer2 = input()
    while answer2 != verbOrganizer.build(fileName)[randomFile][2][randomPropernoun]:
        print("Wrong.")
        points -= 1
        answer2 = input()
    print ("You got it right.")
    points += 1
    round += 1


if round == rounds:
    print("you got",points,"correct")
