print("1")
def div(a, b):
    print("2")
    print(a/b)
    print("3")

def smart_div(func):
    print("4")
    def inner(c, d):
        print("5")
        if c < d:
            print("6")
            c, d = d, c
            print("7")
        return func(c, d)
    print("8")
    return inner


# div1 = smart_div(div)
# div1(2, 4)
print("9")
div = smart_div(div)
print("10")
div(2, 4)
print("11")
