# def greet():
#     print("Hello")
#     print("Good Morning")

# # greet() 
# # greet()



# def add_sub(x, y):
#     c = x + y
#     d = x - y
#     print(c)
#     return c, d


# def add(x, y):
#     c = x + y
#     print(c)
#     return c

# greet()
# result = add(5, 4)
# print(result)

# result2, result3 = add_sub(5, 4)

# print(result2, result3)


#####################################################

# def update(x):
#     print(id(x))
#     x = 8 
#     print(id(x))
#     print("x", x)

# a = 10

# print(id(a))
# update(a)
# print("a", a)

# def update(ls):
#     print(id(lst))
#     lst[1] = 25
#     print(id(lst))
#     print("lst", lst)

# lst = [10, 20, 30]

# print(id(lst))
# update(lst)
# print("lst", lst)

# ######################
# Type of Argument

# def add(a,b):
#     c = a+b
#     print(c)

# add(5,6)

# def person(name, age=18):
    
#     print(name)
#     print(age)

# person('navin', 28)
# person(age = 28, name = "navin")
# person('navin',28)

def add(a, *b):
    c = a
    for i in b:
        c += i
    print(c)


add(5, 6, 7, 3, 9, 10)
add(5)

def add( *b):
    c = 0
    for i in b:
        c += i
    print(c)


add(5, 6, 7, 3, 9, 10)
add(5)

#########################################

def coffes(name,**kwar):
    print(name)
    for i, j in kwar.items():
        print(i, j)

# coffes("navin", 28, "Mumbai", 986432)
coffes("navin", age = 28, city = "Mumbai", mob = 986432)