n = int(input())
solved = 0
for i in range (0,n):
        count1 = 0
        count2 = 0
        y = str(input()).split()
        for x in range(0,len(y)):
            if y[x]=="0":
                count1 = count1 + 1
            elif y[x]=="1":
                count2 = count2 + 1
 
        if(count2 == 3):
            solved = solved + 1
        elif(count2>count1):
            solved = solved + 1
        
        
print(solved)
        

    