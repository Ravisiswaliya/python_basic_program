#implementing stack into python
class Stack():
    def __init__(self):
        self.items = []
    #inserting element into stack
    def push(self, item):
        self.items.append(item)

    #removing element from stack
    def pop(self):
        self.items.pop()
    #checking weather stack is empty or not
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

s = Stack()
s.push('Python')
s.push('Java')
s.push('Java')
s.push('Java')
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.peek())


