
# This Method only works when we are given that majority element do exist in the array
# otherwise this method won't work
def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(1, len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        print("(i=%s, count=%s)" % (i, count))
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]


print(findCandidate([1, 1, 1, 2, 2, 2, 2]))