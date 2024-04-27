''' Prog to check whether a given input is even or by using class called number and
a func with it called check and output with boolean value which has to be apprehended
with as consideration another function to print even or odd'''

class number:
    even=0
    def check(Self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.even_odd(99)


''' wap to segregate all the even numbers and odd numbers seperately with respect to
their lists by taking in consideration of a classs called number and a func using
cinstructor to assign the value of each numver as given inputs into consideration print
seperately in even and odd list '''


class number:
    evens=odds=[]
    def __init__(self,num):
        self.num = num
        if num%2==0:
            num.evens.append(num)
        else:
            num.odds.append(num)
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(56)
n5=number(65)
print("Even numbers are:",number.evens)
print("Odd numbers are:",number.odds)

'''WAP that has a class circle.Use the class var to def the constant pie
Use the class var to calculate area and circumference in diff func with radius 7.5
'''
class circle:
    pie=3.14159
    def __init__(self,r):
        self.r=r
    def area(self,r):
        ca=circle.pie*self.r*self.r
        print("Area is:",ca)
    def circum(self,r):
        cc=2*circle.pie*self.r
        print("Circumference is :",cc)
c=circle(7.5)
c.area(7.5)
c.circum(7.5)
