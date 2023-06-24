# STACK
stack=[]
def push():
    ele=int(input("Enter element:"))
    stack.append(ele)
    print("INSERTION SUCCESFUL")
def pop():
    if not stack:
        print("Stack is Empty")
    else:
        e=stack.pop()
        print("Removed Element:",e)
def display():
    print(stack)
def peek():
    print("PEEK ELEMENT IS:",stack[len(stack)-1])
while True:
    print("Select Operation :\n1.PUSH \n2.POP \n3.DISPLAY STACK \n4.PEEK ELEMENT \n5.EXIT")
    choice=input()
    match choice:
        case '1':
            push()
        case '2':
            pop()
        case '3':
            display()
        case '4':
            peek()
        case '5':
            exit()
        case _:
            print("PLEASE ENTER VALID INPUT")
            
            
        
        
    