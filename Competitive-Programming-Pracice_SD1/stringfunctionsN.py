str='hi'
print(str.center(10,'*'))


str1='JamesBond'
print(str.isalnum())#checking is Alphanumeric or not


str2='7'
print(str2.isdigit())


str='hi'
print(str.ljust(10,'*'))
print(str.rjust(10,'*'))

str3='hifriendz'
print(max(str3))
print(min(str3))



str="MISSISIPI"
print(list(enumerate(str)))

strr="APPLE"
print(strr[::-1])

str='missisipi'
print(str.swapcase())   #changes to lower or higher


str='DANGER'
for letter in str:
    print(letter,end=' ')
    
str=65
print(chr(str))

print(ord('A'))#Gives asccii value


#danger=d+1=e,a+1=b.n+1=o,g+1=h,e+1=f,r+1=s
message="danger"
index=0
while index<len(message):
    letter=message[index]
    print(chr(ord(letter)+1),end=' ')
    index+=1






