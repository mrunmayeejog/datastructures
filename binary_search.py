
def binarysearch(l, key):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == key:
            print("key %d found at position %d" % (key, mid))
            return True
        elif l[mid] < key:
            low = mid + 1
        elif l[mid] > key:
            high = mid - 1

def recursive_bs(a, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        print(mid)
        if a[mid] == key:
            print("key %d found at position %d" % (key, mid))
            return True
        elif a[mid] > key:
            recursive_bs(a, key, low, mid - 1)
        else:
            recursive_bs(a, key, mid+1, high)


l = [4, 11, 18, 30, 54]
found = binarysearch(l, 30)
print("Key in the list: ", found)

a = [1, 7, 19, 26, 38, 56]
f = recursive_bs(a, 38, 0, 5)
print("Key in the listyygyg: ", f)

