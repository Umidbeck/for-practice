class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def push(self, item ):
        self.stack.append(item)
            
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return 'Stack is empty'
            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return 'Stack is empty'
            
obj = Stack()
obj.push('12')
obj.push('11')
obj.push('77')


#print(obj.peek())




def odd_numbers(limit):
    num = 1
    while num <= limit:
        yield num
        num += 2

for number in odd_numbers(10):
    print(number)