i = 0


def rec1():
    global i
    i = i + 1

    print(i, "gfg")
    rec1()


rec1()

# output: RecursionError: maximum recursion depth exceeded while calling a Python object
# c output: segmentation fault
# Java output: stackoverflow
