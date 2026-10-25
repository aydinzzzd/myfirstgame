a= "banana"
i=0
j=0
k=0
for q in range(0,7):
    b=input()
    i=0
    j=0
    k=0
    for p in range(len(b)): 
        if b[p]==a[p]:
            i=i+1
        elif b[p] in a:
            j=j+1        
        else:
            k=k+1
    print(" GREAN:",i,"\n","YELLOW:",j,"\n","RED:",k)
    if b==a:
        break
if b==a:
    print("YOU WON")
else:
    print("YOU LOST")