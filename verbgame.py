import os
import random

import verbOrganizer

try:
    #initializing
    fileName = "verbs"
    round = 0
    points= 0
    rounds = 10 
    lenOFFile = len(verbOrganizer.build(fileName))
    spanishanswers = verbOrganizer.collectSpanishWords("verbs")

    #prints amount of verbs
    print ("there are",lenOFFile,"verbs")

   
   
   
   
    while round < rounds:      
        # changing values every round
        randomMultipleChoices =(random.sample(spanishanswers, k = 5))
        randomAnswer = randomMultipleChoices[random.randrange(0,len(randomMultipleChoices))]
        for i in range (len(verbOrganizer.build(fileName))):
            if randomAnswer == verbOrganizer.build(fileName)[i][0]:
                randomQuestion = verbOrganizer.build(fileName)[i][1]
        #question about spanish word
        print ("What is",randomQuestion,"in spanish.")

        for i in range(len(randomMultipleChoices)):
            print (i+1,randomMultipleChoices[i])

        
        #checking answer
        answer1 = input()
        while answer1 not in "12345":
            print ("invalid input")
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
        print("you got",points,"correct")
except:
    print ("invalid directoy")
    
