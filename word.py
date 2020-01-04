print ("please type a phrase")
word = input()
x=0
y=0
z = False
w = []
l= []
while x < len(word):
   
    if word[x]  in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXXYZ":
        if not z:
            y +=1
            z = True

    if word[x]  in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXXYZ":    
        l.append(word[x])
        
        
    
    
    
    
    
    if word[x] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXXYZ":
        z = False
        
        p = ("".join(l))  
        if l == []:
            pass
        else:
            w.append(p)
        l=[]

    
    
    
    
    
    
    
    
    x += 1

p = ("".join(l))
if l == []:
    pass
else:   
    w.append(p)
    

fwords = (",".join(w))


print ("words: ",y )
print (fwords)
print (w)



m =0
r = 0
checker =  0

while m < len(w):
    currentword = w[m]
    
    while r < len(w):
        if currentword == w[r]:
            checker += 1
        r += 1
    print (currentword,checker)
    m +=1
    checker = 0
    r = 0