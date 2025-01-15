class ExampleClass:
    b = 0
    a = 0
    def __init__(self, val):
        if val % 2 != 0:
            self.a = val
        else:
            self.b = 1


example_object = ExampleClass(11)

print(example_object.a)
print(example_object.b)