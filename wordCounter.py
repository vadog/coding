import os
import random
import verbOrganizer

   #initializing
Dir = "spanishwords"
round = 0
points = 0
rounds = 10
AllWords = verbOrganizer.getData(Dir)
verbData = AllWords[0]
lenOFFile = len(verbData)
#prints amount of verbs
print("there are", lenOFFile, "words")

while round < rounds:
    # changing values every round
    randomVerb = verbData[random.randrange(0, len(verbData))]
    allVerbTenses = []
    for i in range(2,5):

        for tense in randomVerb[i]:
             allVerbTenses.append(tense)
    
    randomMultipleChoices = (random.sample(allVerbTenses, k=5))
    randomAnswer = randomMultipleChoices[random.randrange(0, len(randomMultipleChoices))]   
    randomQuestion = randomVerb[0]
    

    # formating question
    for i in range (2,5):
        if randomAnswer in randomVerb[i]:
            p = i
            if p == 2:
                h = ("present tense")
            if p == 3:
                h = ("preterite tense")
            if p == 4:
                h = ("imperfect tense")
    
    for i in range (2,5):
        for r in range(len(randomVerb[i])):
            if randomAnswer == randomVerb[i][r]:
                if r == 0:
                    propernoun = "yo"
                if r == 1:
                    propernoun = "tu"
                if r == 2:
                    propernoun = "usted"
                if r == 3:
                    propernoun = "nosotros"
                if r == 4:
                    propernoun = "ustedes"
    
    
    # printing question
    print("What is", randomQuestion, "in", h,": ", propernoun)

    for i in range(len(randomMultipleChoices)):
        print(i+1, randomMultipleChoices[i])
    
    
    #checking answer
    answer1 = input()
    while answer1 not in "12345":
        print("invalid input")
        answer1 = input()
    answer1 = int(answer1)
    while randomMultipleChoices[answer1-1] != randomAnswer:
        print("Wrong.")
        break
    else:
        print("You got it right.")
        points += 1
    #adding round
    round += 1
#ending game
if round == rounds:
    print("you got", points, "correct")






