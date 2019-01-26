
def QuickSort(A):
    if len(A) <= 1:
        return A
 
    base = A[0]
    left, right = [], []
    for i in range(1, len(A)):
        (left if A[i] <= base else right).append(A[i])
    return QuickSort(left) + [base] + QuickSort(right)