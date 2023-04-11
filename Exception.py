# # Error
#
# a = 5
# b = 2
# k = int(input("Enter a number"))
# print(k)
# try:
#     print("Resorse Open")
#     print(a/b)
#
# except Exception as e:
#     print("Hey , You cannot divide a Number by Zero", e)
# # print("Bye")
# finally:
#     print("Resorce closed")
#
# Error

a = 5
b = 2

try:
    print("Resorse Open")
    print(a/b)
    k = int(input("Enter a number "))
    print(k)
except ZeroDivisionError as e:
    print("Hey , You cannot divide a Number by Zero", e)
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("something went wrong")
finally:
    print("Resorce closed")

