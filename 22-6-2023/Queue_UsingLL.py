class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
        
a_queue = Queue()
while True:
    print("Enqueue <value>")
    print("Dequeue")
    print("Display")
    #by using split, do will become a list,split
    #works with string
    do = input("What you like to do?").split()
    operation = do[0].strip().lower()
    if operation == ''
    
    
    
    
    