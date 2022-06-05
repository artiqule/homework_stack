class Stack:
    def __init__(self):
        self.stack_list = []

    def isEmpty(self):
        "isEmpty - проверка стека на пустоту. Метод возвращает True или False."
        return bool(self.stack_list)

    def push(self, item):
        "push - добавляет новый элемент на вершину стека. Метод ничего не возвращает."
        self.stack_list.append(item)

    def pop(self):
        "pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека."
        self.stack_list.pop(-1)
        if self.peek() is not False:
            return self.stack_list[-1]
        else:
            pass

    def peek(self):
        "peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется."
        if self.isEmpty() is True:
            return self.stack_list[-1]
        else:
            return False

    def size(self):
        "size - возвращает количество элементов в стеке."
        return len(self.stack_list)


def checking_for_balance(stack_str):
    stack_list = list(stack_str)
    rounded_brackets = Stack()
    curly_braces = Stack()
    square_brackets = Stack()
    for item in stack_list:
        if item == '(':
            rounded_brackets.push(item)
        elif item == ')':
            if rounded_brackets.peek() is not False:
                rounded_brackets.pop()
            else:
                rounded_brackets.push(item)
        if item == '{':
            curly_braces.push(item)
        elif item == '}':
            if curly_braces.peek() is not False:
                curly_braces.pop()
            else:
                curly_braces.push(item)
        if item == '[':
            square_brackets.push(item)
        elif item == ']':
            if square_brackets.peek() is not False:
                square_brackets.pop()
            else:
                square_brackets.push(item)
    if square_brackets.size() == 0 and curly_braces.size() == 0 and rounded_brackets.size() == 0:
        print('Balanced')
    else:
        print('Unbalanced')


if __name__ == '__main__':
    a = "(((([{}]))))"
    b = "[([])((([[[]]])))]{()}"
    c = "{{[()]}}"
    d = "}{}"
    e = "{{[(])]}}"
    f = "[[{())}]"
    checking_for_balance(a)
    print('-'*5)
    checking_for_balance(b)
    print('-'*5)
    checking_for_balance(c)
    print('-'*5)
    checking_for_balance(d)
    print('-'*5)
    checking_for_balance(e)
    print('-'*5)
    checking_for_balance(f)
