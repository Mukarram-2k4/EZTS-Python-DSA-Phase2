#Write a program to create bst for the above list and perform search operation for the given number
#100,
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def search(root, data):
    if root is None:
        return False
    elif root.data == data:
        return True
    elif data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)

list1 = list(map(int,input("Enter List Elements:").split()))
root = None
for i in list1:
    root = insert(root, i)
print(search(root,int(input())))










    
