
class Stack:

    def __init__(self):
        self.lifo = []

    def is_empty(self):
        return len(self.lifo) == 0

    def push(self, item):
        self.lifo.append(item)

    def pop(self):
        return self.lifo.pop()

    def peek(self):
        return self.lifo[-1]

    def size(self):
        return len(self.lifo)


def check_str(my_str: str):
    result = ''
    my_stack = Stack()
    for i, v in enumerate(my_str):
        if len(my_str) % 2 != 0:
            result = 'Несбалансированно'
            break
        if v == '(':
            my_stack.push(')')
        elif v == '[':
            my_stack.push(']')
        elif v == '{':
            my_stack.push('}')
        elif v in [')', ']', '}'] and my_stack.size() != 0 and v == my_stack.peek():
            my_stack.pop()
            if my_stack.size() == 0 and i == len(my_str) - 1:
                result = 'Сбалансированно'
        elif v in [')', ']', '}'] and my_stack.size() != 0 and v != my_stack.peek():
            result = 'Несбалансированно'
            break
        elif v in [')', ']', '}'] and my_stack.size() == 0:
            result = 'Несбалансированно'
            break
        if i == len(my_str) - 1 and my_stack.size() != 0:
            result = 'Несбалансированно'

    return result
