#Lambda function general syntax
# lamda args:expression
sum=lambda x,y:x+y
print("sum=",sum(5,3))

sum=lambda x,y,z:(x+y)-z
print("sum=",sum(5,3,2))


#Program to find smallest number using lambda and  regular function by passing and retyrning args
sum=lambda x,y:x if x<y else y
print(sum(9,5))


def small (a,b):
    if a<b:
        return a
    else:
        return b
sum = lambda x,y:x+y
diff= lambda x,y:x-y
print("smaller value of two exp ls",small(sum(-3,-2),diff(-1,2)))



#Program to use Lambda function within a regular function
def increment(y):
    return(lambda x:x+1)(y)
a=100
print("a before calling lambda in range func=",a)

print("a after calling lambda in range func=",a)
b=increment(a)
print(b)


#sum of 1st 10 Natural Numbers Using Lambda
x=lambda:sum(range(1,11))
print(x)
def names(x,y):
    print(x+y)
names("Mudassir", " Hussain")


def name(fn,ln):
    seperator=' '
    n=fn+seperator+ln
    return n
print(name("Mudassir","Hussain"))




