class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head =Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head = self.head.next
            return popped
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head  #temp = first node
            while temp.next:
                print(temp.data, "-->", end=' ')
                temp = temp.next
            print(temp.data)
    
while True:
    prin