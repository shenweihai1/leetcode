
def min_difference(A):
    return abs(2 * recursion(A, 0, sum(A) / 2) - sum(A))

def recursion(A, idx, rest):
    if idx == len(A) - 1:
        return A[idx] if abs(A[idx] - rest) < abs(rest) else 0


    l = A[idx] + recursion(A, idx + 1, rest - A[idx])
    r = recursion(A, idx + 1, rest)
    return r if abs(l - rest) > abs(r - rest) else l

if __name__ == "__main__":
    A = [1, 6, 11, 5, 2, 4, 2, 23, 4, 9, 32, 13, 3]
    print(min_difference(A))