pos = -1


def search(list_one, n):
    i = 0

    while i<len(list_one):
        if list_one[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False

list_one = [5, 8, 4, 6, 9, 2]
n = 8
if search(list_one, n):
    print("Found at", pos)
else:
    print("Not Found")