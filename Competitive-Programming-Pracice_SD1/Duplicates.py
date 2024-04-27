'''n=[1,1,2,2,3,3,9,4,5,5,7,7,9]
ans=0
for i in range(len(n)):
    ans=ans^n[i]
print(ans)'''

n=[1,1,2,2,3,3,9,4,5,5,7,7,9]
for i in n:
    if(n.count(i)==1):
        print(i)
#Given two sorted arrays a and b.Print them in merge sorted array
l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
l3=l1+l2
t=0
for i in len(l3):
    for j in (len(l3)):
        if(l3[i]<l3[j]):
            t=l3[i]
            l3[i]=l3[j]
            l3[j]=t
        
    
print(l3)
