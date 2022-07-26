import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        # Write code here
        if self.top==-1
              return 1
        else:
            return 0
        
        

    def is_full(self):
        # Write code here
        if self.top==(self.size-1):
            return 1
        else:
            return 0

    def push(self, data):
        if not self.is_full():
            # Write code here
            self.top+=1 self.ist[self.top]=data
            print("ELEMENT IS SUCCESFULLY ADDED")
            else:
                print(("Stack is full")
                      print("cannont push an element")

    def pop(self):
        if not self.is_empty():
            # Write code here
                      t=self.ist[self.top]
                      delself.ist[self.top]
                      self.top-=1
                      return t
                      else:
                      return"stackis empty"
                      return"cannont pop an element"

    def status(self):
        # Write code here
                      for element in self.items:
                      print(element)
                      

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
