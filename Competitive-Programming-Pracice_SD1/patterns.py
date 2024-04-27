for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
print("------------------------------------------------")  
for i in range(4):
    for j in range(8):
        print("*",end=" ")
    print()
print("------------------------------------------------")  
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()
print("------------------------------------------------")
for i in range(1,6):
    for j in range(i):
        print(j+1,end=" ")
    print()
print("------------------------------------------------")  
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
print("------------------------------------------------")
for i in range(6,0):
    for j in range(6):
        print("*",end=" ")
    print()
n=6
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(" * ",end=" ")
    print()
print("------------------------------------------------")
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()   
n=4
for i in range(n+1):
    for j in range(n-i):
        print(' ',end=' ')
    x=1
    for j in range(1,i+1):
        print(x,' ',sep=' ',end=' ')
        x=x*(i-j)//j
    print()
print("------------------------------------------------")
'''n=int(input("Enter rows"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    for l in range(i-1,0,-1):
        print(l,end=' ')
    print()'''
print("------------------------------------------------")
for i in range(1,5):
    for j in range(1,5):
        if i==j or j==1 or i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("------------------------------------------------")
for i in range(1,10):
    for j in range(1,10):
        if i==1 or i==9 or j==1 or j==9:
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()
print("------------------------------------------------")
count=1
for i in range(1,5):
    for j in range(1,5):
        print(count,end=" ")
        count+=1
    print()





