
# Wish OA
def numberOfPairs(A, target):
    # Time complexity: O(nlog(n) + n), asume n = len(A)
    A.sort()
    l, r = 0, len(A) - 1
    ans = set()
    while l < r:
        if A[l] + A[r] == target: 
            ans.add((A[l], A[r]))
            l, r = l + 1, r - 1
        elif A[l] + A[r] < target:
            l += 1
        else: 
            r -= 1
    return len(ans)
    

if __name__ == '__main__':
    A = [1, 2, 3, 6, 7, 8, 9, 1]
    target = 10
    print(numberOfPairs(A, target))