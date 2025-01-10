import sys
class Stack:
    def __init__(self):
            self.__stack_list = []
    def push(self, value):
        self.__stack_list.append(value)
    def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value
    def __str__(self):
        strlist = ""
        for val in self.__stack_list:
            strlist = strlist + str(val) + ", "
        return f"Pila: {strlist}"


stack_object = Stack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)
print(stack_object)
try:
    print(stack_object.pop())
    print(stack_object.pop())
    print(stack_object.pop())
    print(stack_object.pop())
except AttributeError:
    print("el atr es privado")
    sys.exit(1)
except IndexError:
    print("lista out of range")
    sys.exit(1)
