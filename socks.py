n=10
arr=[10,20,20,56,12,25,56,25]
def func(n,arr):
    pair=[]
    arr.sort()
    print(arr)
    if arr[0]==arr[1]:
        pair.append(arr[1])
        print(pair)
    elif arr[1]==arr[2]:
        pair.append(arr[2])
        print(pair)
    elif arr[2] == arr[3]:
        pair.append(arr[3])
        print(pair)
    elif arr[3] == arr[4]:
        pair.append(arr[4])
        print(pair)
    elif arr[4] == arr[5]:
        pair.append(arr[5])
        print(pair)
    elif arr[5] == arr[6]:
        pair.append(arr[6])
        print(pair)
    elif arr[6] == arr[7]:
        pair.append(arr[7])
        print(pair)
    elif arr[7] == arr[8]:
        pair.append(arr[8])
        print(pair)
    elif arr[8] == arr[9]:
        pair.append(arr[9])
        print(pair)
    else:
        print(" chal hatt")
    return pair



b=func(n,arr)
print(type(b))
print(b,"is ")