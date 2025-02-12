def fun_bad(n):
    for i in range(n):
        return i
def fun_good(n):
    for i in range(n):
        yield i
for c in fun_good(5):
    print(c)