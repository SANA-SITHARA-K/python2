num=[2,7,11,15]
target=9
sol=[]
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if (num[i]+num[j])==target:
            sol.append(i)
            sol.append (j)
        print(sol)
    else:
            print("no target")     