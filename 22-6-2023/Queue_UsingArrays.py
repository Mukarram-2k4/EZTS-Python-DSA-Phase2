#queue using array/list
queue=[]
def enqueue():
    ele=input("Enter element")
    queue.append(ele)
    print("Insertion Succesful!!")
def dequeue():
    if not queue:
        print("Queue is Empty")
    else:
        e=queue.pop(0)
        print("Popped ele:",e)
def display():
    print(queue)
while True:
    print("\nSELECT OPERATIONS \n1.ADD \n2.REMOVE \n3.SHOW \n4.QUIT")
    ch=input()
    match ch:
        case '1':
            enqueue()
        case '2':
            dequeue()
        case '3':
            display()
        case '4':
            exit()
            