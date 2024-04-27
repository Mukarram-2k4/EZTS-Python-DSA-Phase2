#obj_name=class name
class abc:
    var=10
    def display(self):
        print("This is in class method")            
obj=abc()
print(obj.var)
obj.display()
#__ method is a constructor class

#----------------------------------------------------------------------
#constructor class
class abcd:
    var=10
    def __init__(self,val):
        self.val = val
        print("This value is",val)            
obj1=abcd(100)

    
