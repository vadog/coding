print ("please type a word")
word = input()
x=0
y=0
z=0
while x < len(word):
    print (word[x])
    if word[x]  in "abcdefghijklmnopqrstuvwxyz":
        if z == 0:
            y +=1
            z +=1
    if word[x] not in "abcdefghijklmnopqrstuvwxyz":
        z = 0
   
   
    x += 1
    
print ("words: ",y )
