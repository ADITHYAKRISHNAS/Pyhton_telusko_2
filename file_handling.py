#
# f = open("MyData", 'r')
#
# # print(f.read())
# print(f.readline(), end="")
# print(f.readline())
#
# f1 = open('abc', 'w')
# f1.write("Something")
# f1.write(" Peaople")

# f1 = open('abc', 'a')
# f1.write("laptop")


f = open('MyData', 'r')

f1 = open('abc', 'w')

for data in f:
    f1.write(data)
    