

def lcs(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return 0

    dp = {}
    for i in range(len(X)):
        dp[(i, len(Y) - 1)] = 1 if Y[len(Y) - 1] in X[i:] else 0

    for j in range(len(Y)):
        dp[(len(X) - 1, j)] = 1 if X[len(X) - 1] in Y[j:] else 0

    ans = 1
    for i in range(len(X) - 1)[::-1]:
        for j in range(len(Y) - 1)[::-1]:
            tmp = 1 + dp[(i + 1, j + 1)] if X[i] == Y[j] else 0
            ans = max(tmp, ans)
            dp[(i, j)] = tmp
    return ans

if __name__ == "__main__":
    X = "IGreeksisgood"
    Y = "MGreeksforGreek"
    print "Length of LCS is ", lcs(X , Y)