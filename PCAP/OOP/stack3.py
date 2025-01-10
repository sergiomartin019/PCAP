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
            strlist = strlist + str(val) + " "
        return f"Pila: {strlist}"

class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0
    def get_sum(self):
        return self.__sum
    def push(self,val):
        self.__sum += val
        Stack.push(self,val)
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)

print(stack_object)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())    