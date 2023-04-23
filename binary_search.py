pos = -1

def search(list_one, n):
    l = 0
    u = len(list_one)-1

    while l <= u:
        mid = (l+u) // 2

        if list_one[mid] == n:
            globals()['pos'] = mid
            return True
        
        else:
            if list_one[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

list_one = [4, 7, 8, 12, 45, 99]

n = 451

if search(list_one, n):
    print("Found at", pos + 1)
else:
    print("Not Found")