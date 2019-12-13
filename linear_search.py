

def linearsearch(list1, key):
    flag = False
    for i in range(len(list1)):
        if key == list1[i]:
            flag = True
            print("Key found at position "+str(i))
            break
    return flag


A = [84, 21, 47, 96, 15]
key = 9
flag = linearsearch(A, key)
if not flag:
    print("Key not found")


def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)


v = factorial(5)
print(v)