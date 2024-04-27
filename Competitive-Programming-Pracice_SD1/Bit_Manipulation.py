'''n=int(input())
if (n & (n-1))==0:
    print("yes")
else:
    print("no")

n=int(input("Enter num:"))
i=int(input("Enter bit position:"))
if n&(1<<i)==0:
    print("no")
else:
    print("yes")
   (or)
n=int(input("Enter num:"))
i=int(input("Enter bit position:))
if n&(1<<i)==0:
    print("no")
else:
    print("yes")

#Given a number n count number of set bits in that number
n=int(input())
count=0
while(n):
    n=n&(n-1)
    count+=1
print(count)
#OR
n=int(input())
count=0
while(n):
    if(n%2!=0):
        count+=1
    n=n>>1
print(count)

#Given an integer A count and return number of trailing zeroes
n=int(input())
count=0
while(1&n!=1):
        count+=1
        n=n>>1
print(count)

#Given A NUMBER n print number of divisors of that number
n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        print(i)
        count+=1
print("No of div=",count)

n=int(input())
i=1
c=0
while(i<=n%i):
    if(n%i==0):
        if(i==n%i):
            c+=1
        else:
            c+=2
    i+=1
print(c)  '''  
       
'''given an array of size n every number is repeated twice except one number.print
that number'''

n=[1,1,2,2,3,3,9,4,5,5,7,7,9]
ans=0
for i in range(len(n)):
    ans=ans^n[i]
print(ans)
       
n=int(input("Enter a Number"))
i=1
count=0
while(i<=(n/i)):
    if(n%i==0):
        if(i==n/i):
            count=count+1
        else:
            count=count+2
    i+=1
print(count)


