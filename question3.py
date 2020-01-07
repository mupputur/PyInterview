"""
Write a python program find sum of  maximum sub list from the given list

Examples :

str1 = "555111000333366666"

"""



class Stack:

    def __init__(self):
        self.x = []

    def is_empty(self):
        if len(self.x) == 0:
            return True
    def top(self):
        return self.x[-1]

    def pushItem(self, ele):
        self.x.append(ele)

    def popItem(self):
        return self.x.pop()
    
    

str1 = "5551110003333556666"
s1 = Stack()
c = 0
for ch in str1:
    if s1.is_empty():
        s1.pushItem(ch)
        c = c+1
    else:
        top = s1.top()
        if top == ch:
            s1.pushItem(ch)
            c = c+1
        else:
            s1.pushItem(str(c))
            s1.pushItem(ch)
            c = 1
s1.pushItem(str(c))
print("".join(s1.x))
        
    
