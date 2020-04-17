print ("please type name of txt file")
fileName = input()

theFile = open(fileName, "r")
fileContent = theFile.read()
theFile.close()


x=0
numWords=0
z = False
w = []
currentWordCars= []
count = 0

validCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXXYZ0123456789"

while x < len(fileContent):
   
    if fileContent[x]  in validCharacters :
        currentWordCars.append(fileContent[x])
        if not z:
            numWords +=1
            z = True
    else:
        z = False
        
        p = ("".join(currentWordCars))  
        if currentWordCars == []:
            pass
        else:
            w.append(p)
        currentWordCars=[]
  
    x += 1
# deal with last words
p = ("".join(currentWordCars))
if currentWordCars == []:
    pass
else:   
    w.append(p)
    
fwords = (",".join(w))

with open(fileName, 'r') as f:
    for line in f:
        count += 1

print ("words: ",numWords )
print("Total number of lines is: ", count)
print (fwords)





