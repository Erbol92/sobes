class Stack:

    def __init__(self, val: list):
        self.items = val

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return 'пустой список'

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'пустой список'

    def size(self):
        return len(self.items)

    def balansed(self):
        # список хранения открыв. скобок
        stack = []
        brackets = {')': '(',
                    '}': '{',
                    ']': '['
                    }

        items = self.items
        if not len(items) % 2 == 0:
            return 'Несбалансированно'

        for char in items:
            if char in brackets.values():  # если открывающая скобка
                stack.append(char)
            elif char in brackets.keys():  # если закрывающая скобка
                if stack == [] or brackets[char] != stack.pop():
                    return 'Несбалансированно'
        if not stack:
            return 'Сбалансированно'


strings = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{}",
    "{{[(])]}}",
    "[[{())}]"]

if __name__ == '__main__':
    for string in strings:
        obj = Stack(string)
        print(obj.balansed())
