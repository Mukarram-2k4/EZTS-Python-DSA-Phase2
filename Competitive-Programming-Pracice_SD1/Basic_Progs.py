#1 Remove duplicates from list
l1=list(map(int,input().split()))
non_dup=[]
for i in l1:
    if i not in non_dup:
        non_dup.append(i)
print(*non_dup)

#2 Calculate Electricity Bill
a=int(input())
n=a//100
sum1=(a%100)*(n+1)    
sum1=sum1 + (((n*(n+1))/2)*100)
print(sum1)

#3Calculate Hours minutes and seconds for a given no of seconds
n=int(input())
h=a//3600
m=(a%3600)//60
s=(a%3600)%60
print(h,m,s)

#4 Remove consecutive dulpicates(Sliding Window Method)
a=input()
n=""
for i in range(0,len(a)-1):
    if a[i]!=a[i+1]:
        print(a[i],end="")
print(a[-1])

#5 Decoding the given String
a="bvec"
n=4
for i in a:
    if(ord(i)-n <97):
        print(chr(ord(i)-n+26),end="")
    else:
        print(chr(ord(i)-n),end="")       
#6
a=list(map(int,input().split()))
max=0
c=0
for i in a:
    if(i%2==0):
        c=c+1
    else:
        if(c>max):
            max=c
        c=0
if(c>max):
    max=c
print(max)

#7
a=str(input())
b=1
ans=1
for i in range (len(a)-1):
    if chr(ord(a[i]))==chr(ord(a[i+1])-1):
        b=b+1
    else:
        if (b>ans):
            ans=b
        b=1
if b>ans:
    ans=b
print(ans)

# print yes if input is sorted and no otherwise

l = list(map(int, input().split()))
flag = 0
for i in range(1, len(l)-1):
  if(l[i] < l[i-1]):
    print('no')
    flag = 1
    break
if(flag == 0):
  print('yes')
  
#---------------
a=input().split(",")
b=""
for i in a:
    i=i.split(":")
    if(str(len(i[0]))) in i[1]:
        b=b+i[0][-1]
    else:
        d=0;c=0
        for j in i[1]:
            if(int(j)<len(i[0])):
                d=int(j)
                if(int(j)>d):
                    d=int(j)
        if(c==1):
            b=b+i[0][d-1]
        else:
            b=b+"x"               
print(b)

#-----------------
a=input()
b=[]
for i in a:
    if(i.isalpha()):
        b.append(i)
b=b[::-1]
for i in range(len(a)):
    if(not a[i].isalpha()):
        b.insert(i,a[i])
print("".join(b))

#---------------------
l1=list(map(int,input().split()))
n=int(input())
l2=l1.copy()
l2.sort()
print(l1.index(n) - l2.index(n))
#--------------------

l1=list(map(int,input().split()))
n=int(input())
l1.sort()
print(l1[-n])
#---------------------
l1=list(map(int,input().split()))
n=int(input())
l2=l1[0:n]
l3=l1[n:]
l2.sort()
l3.sort(reverse=True)
print(l2+l3)

a=input()
l1=[]
for i in a:
    if(not i.isalpha()):
       l1.append(int(i))
l1.sort(reverse=True)
print(" ".join(str(l1)))


    
    






