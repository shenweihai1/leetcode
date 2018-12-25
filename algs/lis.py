

def lis(A):
    if len(A) == 0: return 0
    dp = [1]
    for i in range(1, len(A)):
        dp.append(max([1 if A[i] < A[j] else dp[j] + 1 for j in range(0, i)]))

    return max(dp)


if __name__ == "__main__":
    print(lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))