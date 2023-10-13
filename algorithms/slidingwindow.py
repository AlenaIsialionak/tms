def slidingWindow_max(arr, k):
    n = len(arr)
    sp_max = []
    for i in range(n-k+1):
        max_elem = arr[i]
        for j in range(k):
            if arr[j+i] > max_elem:
                max_elem = arr[j+i]
        sp_max.append(max_elem)
    return sp_max

def slidingWindow_middle(arr, k):
    n = len(arr)
    sp_middle = []
    sp = []
    if k % 2 == 0:
        ind1, ind2 = (k // 2 - 1), k // 2
        for i in range(n-k+1):
            sp = arr[i:i+k]
            sp.sort()
            sp_middle.append((sp[ind1]+sp[ind2])/2)
        return sp_middle
    else:
        ind = k//2
        for i in range(n-k+1):
            sp = arr[i:i+k]
            sp.sort()
            sp_middle.append(sp[ind])
        return sp_middle



# print(slidingWindow_max([1, 3, -1, -3, -5, 3, 6, 7], 3))
# print(slidingWindow_max([1], 1))

# Sliding Window Median
# print(slidingWindow_middle([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
print(slidingWindow_middle([1, 2, 3, 4], 4))

