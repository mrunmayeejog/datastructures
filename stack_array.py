
class ArrayStack():
    def __init__(self):
        self.data = []

    def lenth(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, ele):
        self.data.append(ele)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.data.pop()

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.data[-1]




s = ArrayStack()
s.push(10)
s.push(20)
s.push(30)
print("Stack elements : ", s.data)
print("top of stack", s.top())
print("is stack empty ? ", s.is_empty())
print("length of stack ", s.lenth())
print("Element popped ", s.pop())
print("stack data", s.data)
print("Element popped ", s.pop())
print("stack data", s.data)
print("top of stack", s.top())
print("Element popped ", s.pop())
print("stack data", s.data)
print("top of stack", s.top())
