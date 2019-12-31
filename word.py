print ("please type a phrase")
word = input()
x=0
y=0
z = False
w = []
while x < len(word):
   
    if word[x]  in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXXYZ":
        if not z:
            y +=1
            z = True
    if word[x] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXXYZ":
        z = False
   
    w.append(word[x])

    x += 1
    
print ("words: ",y )
print ("".join(w))