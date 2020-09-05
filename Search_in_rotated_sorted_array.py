def search(A, target):
    if len(A) == 0:
        return -1
    start = 0
    end = len(A) - 1
    while start + 1 < end:
        mid = int(start + (end - start) / 2)
        if A[mid] == target:
            return mid
        # here m in green line,ascent array in here and then in this arrange you can find the target using binary search
        if A[mid] > A[start]:
            if A[start] <= target and target <= A[mid]:
                end = mid
            else:
                 start = mid
        # here m in red line (bot
        # tom)
        else:
            if A[end] >= target and target >= A[mid]:
                start = mid
            else:
                end = mid
    if A[start] == target:
        return start
    elif A[end] == target:
        return end
    else:
        return -1
A=[1002,10203,9,10,100,101]
print (search(A,9))








